from google.adk.tools import BaseTool
from git import Repo
import os

class GitHubCloneTool(BaseTool):
    def __init__(self):
        super().__init__(
            name="GitHubCloneTool",
            description="Clones a GitHub repository to a local directory"
        )

    def run(self, repo_url: str) -> str:
        repo_name = repo_url.split("/")[-1].replace(".git", "")
        clone_path = f"./outputs/{repo_name}"
        if os.path.exists(clone_path):
            os.system(f"rm -rf {clone_path}")
        Repo.clone_from(repo_url, clone_path)
        return f"Repository cloned to {clone_path}"
