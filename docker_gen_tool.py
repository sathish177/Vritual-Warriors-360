from google.adk.tools import BaseTool

class DockerGenTool(BaseTool):
    def __init__(self):
        super().__init__(
            name="DockerGenTool",
            description="Generates a Dockerfile for the given stack"
        )

    def run(self, stack_description: str) -> str:
        if "Python" in stack_description:
            dockerfile = """FROM python:3.10
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]"""
        elif "Node.js" in stack_description:
            dockerfile = """FROM node:18
WORKDIR /app
COPY . .
RUN npm install
EXPOSE 3000
CMD ["npm", "start"]"""
        else:
            dockerfile = "FROM ubuntu\n# TODO: Add custom setup"

        with open("outputs/Dockerfile", "w") as f:
            f.write(dockerfile)

        return "Dockerfile generated at outputs/Dockerfile"
