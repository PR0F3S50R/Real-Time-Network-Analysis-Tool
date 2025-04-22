import requests

def call_deepseek(prompt):
    url = "http://localhost:1234/v1/completions"
    payload = {
        "prompt": prompt,
        "max_tokens": 150,
        "temperature": 0.2
    }
    response = requests.post(url, json=payload)
    if response.ok:
        return response.json().get("choices", [{}])[0].get("text", "").strip()
    else:
        print("LLM error:", response.text)
        return "{}"
