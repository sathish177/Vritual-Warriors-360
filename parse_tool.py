from google.adk.tools import BaseTool
import os

class StackDetectionTool(BaseTool):
    def __init__(self):
        super().__init__(
            name="StackDetectionTool",
            description="Detects the technology stack of the repository"
        )

    def run(self, repo_path: str) -> str:
        files = os.listdir(repo_path)
        tech_stack = []

        if "package.json" in files:
            tech_stack.append("Node.js")
        if "requirements.txt" in files:
            tech_stack.append("Python")
        if "pom.xml" in files:
            tech_stack.append("Java (Maven)")

        return f"Detected tech stack: {', '.join(tech_stack)}"
