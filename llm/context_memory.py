# In-memory dynamic context retraining (few-shot prompt updating)
prompt_bank = []

def add_to_context(log, verdict, reason):
    prompt_bank.append({"log": log, "verdict": verdict, "reason": reason})
    if len(prompt_bank) > 10:
        prompt_bank.pop(0)

def generate_dynamic_prompt(new_log):
    few_shots = "\n".join([
        f"Input: {item['log']}\nResponse: {{\"verdict\": \"{item['verdict']}\", \"reason\": \"{item['reason']}\"}}"
        for item in prompt_bank
    ])
    return f"{few_shots}\nInput: {new_log}\nResponse:"
