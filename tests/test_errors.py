"""Malformed source files must return a usable MCP tool error."""

import tempfile
import unittest
from pathlib import Path

from mcp.server.mcpserver.exceptions import ToolError

from arc_engineering.files import Workspace
from arc_engineering.server import expected_errors


class InputErrorTests(unittest.TestCase):
    def test_malformed_archives_and_pdf_return_actionable_errors(self):
        with tempfile.TemporaryDirectory() as directory:
            workspace = Workspace(directory)
            read = expected_errors(workspace.read_file)
            for suffix in ("xlsx", "docx", "pdf"):
                Path(directory, "bad." + suffix).write_bytes(b"invalid document")
                with self.subTest(suffix=suffix), self.assertRaises(ToolError) as error:
                    read("bad." + suffix)
                self.assertTrue(str(error.exception))


if __name__ == "__main__":
    unittest.main()
