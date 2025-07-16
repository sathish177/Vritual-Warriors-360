
from agent import agent

while True:
    user_input = input("\nAutoDockAgent > ")
    if user_input.lower() in ["exit", "quit"]:
        break
    response = agent.run(user_input) 
    print(response.output)

   