import sys
import os

# Adds the project root to the search path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agents.base_agent import BaseAgent
from tools.business_tools import (
    analyze_revenue,
    customer_segmentation,
    suggest_kpis
)


class ToolAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Tool Agent",
            system_prompt="""
You are a business execution agent.

Your job is to execute a given task and provide a clear, actionable result.

Rules:
- Be practical
- Use tools when applicable
- Otherwise use reasoning
"""
        )

    def use_tool(self, task: str):
        """
        Decide and execute tool based on task
        """
        task_lower = task.lower()

        try:
            # 🔧 Revenue Tool
            if "revenue" in task_lower:
                data = {
                    "revenue": 12000,
                    "previous_revenue": 10000
                }
                return analyze_revenue(data)

            # 🔧 Customer Segmentation
            elif "customer" in task_lower:
                customers = [
                    {"name": "A", "spend": 1200},
                    {"name": "B", "spend": 700},
                    {"name": "C", "spend": 300}
                ]
                return customer_segmentation(customers)

            # 🔧 KPI Suggestion
            elif "kpi" in task_lower or "metric" in task_lower:
                return suggest_kpis("ecommerce")

            else:
                return None

        except Exception as e:
            return f"Tool Error: {str(e)}"

    def execute_task(self, task: str) -> str:
        """
        Execute task using tool or LLM
        """
        tool_result = self.use_tool(task)

        if tool_result:
            return f"[TOOL OUTPUT]\n{tool_result}"
        else:
            return f"[LLM OUTPUT]\n{self.run(task)}"

    def run_tasks(self, tasks: list):
        """
        Execute all tasks
        """
        results = []

        for i, task in enumerate(tasks, 1):
            print(f"\n🔧 Executing Task {i}: {task}")

            result = self.execute_task(task)

            results.append({
                "task": task,
                "result": result
            })

        return results


# 🔥 TEST BLOCK
if __name__ == "__main__":
    agent = ToolAgent()

    print("Running Hybrid Tool Agent...\n")

    tasks = [
        "Analyze revenue performance",
        "Segment customers based on spending",
        "Suggest important KPIs",
        "Create a marketing strategy"
    ]

    outputs = agent.run_tasks(tasks)

    print("\nFinal Results:\n")

    for item in outputs:
        print(f"Task: {item['task']}")
        print(f"Result: {item['result']}\n")