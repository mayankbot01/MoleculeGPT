import os
from dotenv import load_dotenv
from minion.agent import MinionAgent

def main():
    load_dotenv()
    
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY not found in environment.")
        return

    agent = MinionAgent()
    print("Minion System Replica initialized. Type 'exit' to quit.")
    
    while True:
        task = input("What can I help you with? ")
        if task.lower() in ["exit", "quit"]:
            break
        
        print("\nProcessing task...")
        result = agent.run(task)
        print(f"\nMinion: {result}\n")

if __name__ == "__main__":
    main()
