from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from llm.prompt_formatter import format_prompt
from llm.deepseek_caller import call_deepseek
from output.webhook_handler import handle_output
import time

class LogHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith(".log"):
            with open(event.src_path, "r") as f:
                lines = f.readlines()
                if lines:
                    prompt = format_prompt(lines[-1])
                    result = call_deepseek(prompt)
                    handle_output(result)

def start_log_monitor(path="/var/log"):
    observer = Observer()
    observer.schedule(LogHandler(), path=path, recursive=False)
    observer.start()
    print(f"Monitoring logs in {path}")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
