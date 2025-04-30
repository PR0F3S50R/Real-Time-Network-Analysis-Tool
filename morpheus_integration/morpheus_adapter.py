# Simulated Morpheus-like flow (lightweight version)

def handle_uncertain_logs(log):
    from llm.prompt_formatter import format_prompt
    from llm.deepseek_caller import call_deepseek
    from output.webhook_handler import handle_output

    prompt = format_prompt(log)
    result = call_deepseek(prompt)
    handle_output(result)

# In a real Morpheus flow, this would be a hook into Triton decision scores
