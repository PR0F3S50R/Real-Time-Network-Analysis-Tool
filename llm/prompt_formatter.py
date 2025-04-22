def format_prompt(log_or_packet):
    return f"""You are a cybersecurity AI. Analyze the following input and classify it as "normal" or "malicious". Return JSON:
Input: {log_or_packet}
Response format: {{\"verdict\": \"...\", \"reason\": \"...\"}}
"""
