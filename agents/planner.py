import sys
import os

# Adds the project root to the search path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agents.base_agent import BaseAgent
import json


class PlannerAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Planner Agent",
            system_prompt="""
You are an expert business planner.

Your job is to break down a user request into clear, step-by-step actionable tasks.

Rules:
- Return ONLY a JSON list
- Each step should be short and actionable
- No explanations
- No extra text
- Example:
["Step 1", "Step 2", "Step 3"]
"""
        )

    def parse_response(self, response: str):
        """
        Convert LLM response to Python list safely
        """
        try:
            return json.loads(response)
        except json.JSONDecodeError:
            # Fallback: clean text into list
            lines = response.split("\n")
            steps = [line.strip("- ").strip() for line in lines if line.strip()]
            return steps

    def run(self, user_input: str):
        raw_response = super().run(user_input)
        steps = self.parse_response(raw_response)
        return steps


# 🔥 TEST BLOCK
if __name__ == "__main__":
    planner = PlannerAgent()

    print("Running Planner Agent...\n")

    task = "Increase sales of an online clothing store"

    steps = planner.run(task)

    print("Generated Plan:\n")
    for i, step in enumerate(steps, 1):
        print(f"{i}. {step}")