from google.adk.agents import LlmAgent
from tools.github_tool import GitHubCloneTool
from tools.parse_tool import StackDetectionTool
from tools.docker_gen_tool import DockerGenTool
from tools.test_tool import DockerValidatorTool

agent = LlmAgent(
    name="AutoDockAgent",
    description="An agent that clones GitHub repos and generates Dockerfiles",
    tools=[
        GitHubCloneTool(),
        StackDetectionTool(),
        DockerGenTool(),
        DockerValidatorTool()
    ]
)
