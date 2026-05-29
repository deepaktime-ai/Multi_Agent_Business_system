import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from llm.ollama_client import OllamaClient


class BaseAgent:
    def __init__(self, name: str, system_prompt: str):
        self.name = name
        self.system_prompt = system_prompt
        self.llm = OllamaClient()

    def build_prompt(self, user_input: str) -> str:
        """
        Combine system prompt + user input
        """
        return f"""
You are {self.name}.

{self.system_prompt}

User Request:
{user_input}

Response:
"""

    def run(self, user_input: str) -> str:
        """
        Main execution method for all agents
        """
        prompt = self.build_prompt(user_input)

        response = self.llm.generate(prompt)

        return response


# 🔥 TEST BLOCK
if __name__ == "__main__":
    agent = BaseAgent(
        name="Test Agent",
        system_prompt="You are a helpful business assistant."
    )

    print("Running Base Agent...\n")

    result = agent.run("Give me 3 business ideas.")

    print("Response:\n")
    print(result)