from google.adk.tools import BaseTool
import subprocess

class DockerValidatorTool(BaseTool):
    def __init__(self):
        super().__init__(
            name="DockerValidatorTool",
            description="Builds the Dockerfile to check if it works"
        )

    def run(self, path: str = "./outputs") -> str:
        try:
            result = subprocess.run(
                ["docker", "build", "-t", "auto-dock-it", "."],
                cwd=path,
                capture_output=True,
                text=True,
                check=True
            )
            return "Docker build succeeded:\n" + result.stdout
        except subprocess.CalledProcessError as e:
            return "Docker build failed:\n" + e.stderr
