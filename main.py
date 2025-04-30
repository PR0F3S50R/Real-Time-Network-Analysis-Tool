from ingest.log_watchdog import start_log_monitor
from ingest.scapy_sniffer import start_sniffer

if __name__ == "__main__":
    start_log_monitor()
    start_sniffer()
