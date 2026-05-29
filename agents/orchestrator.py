import sys
import os

# Add the project root (Multi_Agent_Business_system) to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Now your import will work perfectly
from agents.planner import PlannerAgent
from agents.tool_agent import ToolAgent
from agents.memory import MemoryAgent


class OrchestratorAgent:
    def __init__(self):
        self.planner = PlannerAgent()
        self.tool_agent = ToolAgent()
        self.memory = MemoryAgent()

    def run(self, user_input: str):
        print("\n🧠 Orchestrator started...\n")

        # Step 1: Planning
        print("📌 Planning tasks...\n")
        plan = self.planner.run(user_input)

        if not plan or len(plan) == 0:
            return "Error: Planning failed."

        # Step 2: Execution
        print("⚙️ Executing tasks...\n")
        results = self.tool_agent.run_tasks(plan)

        # Step 3: Save Memory
        print("\n💾 Saving to memory...\n")
        self.memory.add_entry(user_input, plan, results)

        # Step 4: Final Response
        final_output = {
            "user_input": user_input,
            "plan": plan,
            "results": results
        }

        return final_output


# 🔥 TEST BLOCK
if __name__ == "__main__":
    orchestrator = OrchestratorAgent()

    print("🚀 Running Full Multi-Agent System...\n")

    user_query = "Increase sales for a small online business"

    output = orchestrator.run(user_query)

    print("\n✅ FINAL OUTPUT:\n")

    print("User Input:")
    print(output["user_input"], "\n")

    print("Plan:")
    for i, step in enumerate(output["plan"], 1):
        print(f"{i}. {step}")

    print("\nResults:")
    for item in output["results"]:
        print(f"\nTask: {item['task']}")
        print(f"Result: {item['result']}")