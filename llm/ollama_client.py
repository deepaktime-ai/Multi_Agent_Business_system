import requests
import json

class OllamaClient:
    def __init__(self, model="llama3", base_url="http://localhost:11434"):
        self.model = model
        self.base_url = base_url

    def generate(self, prompt: str) -> str:
        """
        Send prompt to Ollama and return response text
        """
        url = f"{self.base_url}/api/generate"

        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }

        try:
            response = requests.post(url, json=payload, timeout=60)

            # Debug: HTTP error
            if response.status_code != 200:
                return f"Error: Ollama API returned status {response.status_code} - {response.text}"

            data = response.json()

            # Debug: Missing response
            if "response" not in data:
                return "Error: Invalid response format from Ollama"

            return data["response"].strip()

        except requests.exceptions.ConnectionError:
            return "Error: Cannot connect to Ollama. Is it running?"

        except requests.exceptions.Timeout:
            return "Error: Ollama request timed out"

        except Exception as e:
            return f"Unexpected Error: {str(e)}"


# 🔥 TEST BLOCK (VERY IMPORTANT)
if __name__ == "__main__":
    client = OllamaClient()

    print("Testing Ollama connection...\n")

    test_prompt = "Explain business growth strategy in 2 lines."

    result = client.generate(test_prompt)

    print("Response:\n")
    print(result)