from agent import agent
from envs import init_env

init_env()
print("✅ AutoDockAgent is running. Type your command below:\n")

while True:
    try:
        user_input = input("AutoDockAgent > ")
        response = agent.run(user_input)
        print(response)
    except KeyboardInterrupt:
        print("\n👋 Exiting AutoDockAgent.")
        break
