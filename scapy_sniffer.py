from scapy.all import sniff
from llm.prompt_formatter import format_prompt
from llm.deepseek_caller import call_deepseek
from output.webhook_handler import handle_output

def handle_packet(pkt):
    summary = pkt.summary()
    prompt = format_prompt(summary)
    result = call_deepseek(prompt)
    handle_output(result)

def start_sniffer():
    print("Starting packet sniffer...")
    sniff(filter="tcp", prn=handle_packet, store=0)
