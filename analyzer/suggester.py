import requests
import os

class AICodeSuggester:
    def __init__(self, api_key):
        self.api_key = api_key
        self.url = "https://api.groq.com/openai/v1/chat/completions"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def suggest_fixes(self, user_code, issue):
        prompt = f"""You are a helpful assistant that reviews Python DSA code.
The following code has a problem:

{user_code}"""

        payload = {
    "model": "llama3-70b-8192",  # Supported model
    "messages": [
        {"role": "system", "content": "You are a Python DSA expert."},
        {"role": "user", "content": prompt}
    ],
    "temperature": 0.2
        }
        response = requests.post(self.url, headers=self.headers, json=payload)
        response = requests.post(self.url, headers=self.headers, json=payload)
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            raise Exception(f" Groq API Error: {response.status_code}\n{response.text}")
