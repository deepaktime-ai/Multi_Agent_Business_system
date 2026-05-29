import json
import os


class MemoryAgent:
    def __init__(self, file_path="data/memory.json"):
        self.file_path = file_path
        self._ensure_file()

    def _ensure_file(self):
        """
        Ensure memory file exists and is valid
        """
        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as f:
                json.dump([], f)

    def load_memory(self):
        """
        Load memory safely
        """
        try:
            with open(self.file_path, "r") as f:
                return json.load(f)
        except:
            return []

    def save_memory(self, data):
        """
        Save memory safely
        """
        with open(self.file_path, "w") as f:
            json.dump(data, f, indent=4)

    def add_entry(self, user_input, plan, results):
        """
        Store a new interaction
        """
        memory = self.load_memory()

        entry = {
            "user": user_input,
            "plan": plan,
            "results": results
        }

        memory.append(entry)
        self.save_memory(memory)

    def get_recent_context(self, n=3):
        """
        Get last N interactions
        """
        memory = self.load_memory()
        return memory[-n:]


# 🔥 TEST BLOCK
if __name__ == "__main__":
    memory = MemoryAgent()

    print("Testing Memory Agent...\n")

    # Sample data
    user_input = "Improve online sales"
    plan = ["Analyze data", "Improve ads"]
    results = ["Target audience identified", "Ad strategy created"]

    memory.add_entry(user_input, plan, results)

    print("Recent Memory:\n")
    context = memory.get_recent_context()

    for item in context:
        print(item)