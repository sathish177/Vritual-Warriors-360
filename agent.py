import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from google.adk.agents import LlmAgent
from  tools.github_tool import GitHubCloneTool
from tools.parse_tool import StackDetectionTool
from tools.docker_gen_tool import DockerGenTool
from tools.test_tool import DockerValidatorTool

agent = LlmAgent(
    name="AutoDockAgent",
    description="Agent that automates GitHub repo analysis and Docker setup.",
    tools=[
        GitHubCloneTool(),
        StackDetectionTool(),
        DockerGenTool(),
        DockerValidatorTool(),
    ]
)
