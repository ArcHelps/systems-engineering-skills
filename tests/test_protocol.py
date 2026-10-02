"""Test the actual stdio transport rather than only Python functions."""

import tempfile
import unittest
from pathlib import Path
import sys

import anyio
from mcp import Client, StdioServerParameters


class ProtocolTests(unittest.TestCase):
    def test_stdio_discovery_prompt_resources_and_file_tool(self):
        async def exercise():
            with tempfile.TemporaryDirectory() as directory:
                Path(directory, "req.csv").write_text("ID,Text\nR1,The system shall respond.\n")
                params = StdioServerParameters(
                    command=sys.executable,
                    args=["-m", "arc_engineering", "serve", "--workspace", directory],
                )
                async with Client(params) as client:
                    tools = await client.list_tools()
                    self.assertIn("import_requirements", {tool.name for tool in tools.tools})
                    prompts = await client.list_prompts()
                    self.assertEqual(len(prompts.prompts), 100)
                    name = prompts.prompts[0].name
                    prompt = await client.get_prompt(name, {"input": "Synthetic engineering input"})
                    self.assertIn("Synthetic engineering input", prompt.messages[0].content.text)
                    resource = await client.read_resource("arc://catalog")
                    self.assertTrue(resource.contents[0].text)
                    result = await client.call_tool("read_file", {"path": "req.csv"})
                    self.assertFalse(result.is_error)
                    bad = await client.call_tool("read_file", {"path": "/etc/passwd"})
                    self.assertTrue(bad.is_error)
                    imported = await client.call_tool(
                        "import_requirements",
                        {"path": "req.csv", "mapping": {"id": "ID", "statement": "Text"}},
                    )
                    self.assertFalse(imported.is_error)
                    capabilities = client.server_capabilities.model_dump(by_alias=True)
                    self.assertIn("io.modelcontextprotocol/skills", capabilities["extensions"])

    def test_large_import_can_save_a_complete_proposal_and_return_bounded_summary(self):
        async def exercise():
            import csv
            import json

            with tempfile.TemporaryDirectory() as directory:
                with Path(directory, "large.csv").open("w", newline="") as stream:
                    writer = csv.writer(stream)
                    writer.writerow(["ID", "Text"])
                    writer.writerows(
                        (f"R{i}", "The subsystem shall report status.") for i in range(5000)
                    )
                params = StdioServerParameters(
                    command=sys.executable,
                    args=["-m", "arc_engineering", "serve", "--workspace", directory],
                )
                async with Client(params) as client:
                    result = await client.call_tool(
                        "import_requirements",
                        {
                            "path": "large.csv",
                            "mapping": {"id": "ID", "statement": "Text"},
                            "proposal_path": "proposal.json",
                        },
                    )
                    self.assertFalse(result.is_error)
                    summary = json.loads(result.content[0].text)
                    self.assertEqual(summary["counts"]["imported"], 5000)
                    self.assertEqual(summary["artifact"]["path"], "proposal.json")
                    saved = json.loads(Path(directory, "proposal.json").read_text())
                    self.assertEqual(len(saved["model"]["items"]), 5000)
                    self.assertEqual(saved["counts"]["source_records"], 5000)
                    retry = await client.call_tool(
                        "import_requirements",
                        {
                            "path": "large.csv",
                            "mapping": {"statement": "Text"},
                            "proposal_path": "proposal.json",
                        },
                    )
                    self.assertTrue(retry.is_error)
                    self.assertEqual(
                        json.loads(Path(directory, "proposal.json").read_text()), saved
                    )

        anyio.run(exercise)

        anyio.run(exercise)


if __name__ == "__main__":
    unittest.main()
