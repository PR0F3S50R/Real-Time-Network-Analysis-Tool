import json
from llm.context_memory import add_to_context

log_path = "dashboard/data.json"

def handle_output(response_text, original_log=None):
    try:
        data = json.loads(response_text)
        verdict = data.get("verdict")
        reason = data.get("reason")
        print(f"[{verdict.upper()}] - {reason}")
        add_to_context(original_log, verdict, reason)

        # Save to dashboard
        entry = {"log": original_log, "verdict": verdict, "reason": reason}
        try:
            with open(log_path, "r") as f:
                all_data = json.load(f)
        except:
            all_data = []

        all_data.append(entry)
        with open(log_path, "w") as f:
            json.dump(all_data[-100:], f)
    except Exception as e:
        print("Output parsing error:", e)
