# DeepSeek Morpheus Analyzer 🧠⚡

A real-time network traffic and system log analysis pipeline powered by the **DeepSeek-Code-V2-Lite-Instruct** local LLM, integrated with **NVIDIA Morpheus** and deployable via **Triton Inference Server**.

Built for lightweight systems (Ryzen 7, RTX 3050 4GB), this project classifies network traffic and logs as **malicious** or **benign** using a locally hosted LLM, with real-time results displayed in a custom Flask dashboard.

---

## 🚀 Features

- ✅ **Real-Time Inference:** Classifies log files and sniffed network packets on the fly
- 🔍 **Few-shot Context Memory:** Dynamic sliding window of previous samples to enhance LLM understanding
- 📺 **Web Dashboard:** Live status display with auto-refreshing logs and highlight for threats
- 🐳 **Docker-Ready:** Full Docker Compose stack with Triton, Flask UI, Analyzer, and memory context
- 🧠 **DeepSeek LLM via LM Studio:** Lightweight, accurate local inference
- ⚙️ **Morpheus-Ready Adapter:** Future-ready with GPU-based pipeline using NVIDIA Morpheus

---

## 📦 Technologies Used

- [DeepSeek-Code-V2-Lite-Instruct](https://github.com/deepseek-ai/DeepSeek-Coder)
- [NVIDIA Morpheus](https://developer.nvidia.com/morpheus)
- [Triton Inference Server](https://github.com/triton-inference-server/server)
- Python, Flask, Scapy, Watchdog, Docker, OpenAI-compatible API


## 🏛️ Architechtural Design 


                               ┌───────────────────────────┐
                               │     User/Analyst UI       │
                               │   Flask Web Dashboard     │
                               └────────────┬──────────────┘
                                            │
                            HTTP Poll (logs, results, memory state)
                                            │
                                            ▼
┌──────────────────────────────────────────────────────────────────────┐
│                        DeepSeek Morpheus Analyzer                    │
├──────────────────────────────────────────────────────────────────────┤
│                                                                      │
│   ┌──────────────┐     ┌────────────────────────────┐                │
│   │  Watchdog    │     │        Scapy Sniffer       │                │
│   │ (File Logs)  │     │ (Live Network Traffic)     │                │
│   └────┬─────────┘     └──────┬─────────────────────┘                │
│        │                      │                                      │
│        ▼                      ▼                                      │
│ ┌──────────────┐    ┌────────────────┐                               │
│ │ Log Parser   │    │ Packet Parser  │                               │
│ └────┬─────────┘    └────┬───────────┘                               │
│      ▼                      ▼                                        │
│           ┌────────────────────────────┐                            │
│           │     Sample Queue Buffer    │◄────┐                      │
│           └────────────┬───────────────┘     │                      │
│                        ▼                     │                      │
│           ┌───────────────────────────┐      │                      │
│           │  Sliding Context Manager  │──────┘                      │
│           └────────────┬──────────────┘                             │
│                        ▼                                            │
│               ┌──────────────────────┐                              │
│               │ LLM Inference Module │                              │
│               │ DeepSeek via LMStudio│                              │
│               └────────┬─────────────┘                              │
│                        ▼                                            │
│        ┌─────────────────────────────┐                              │
│        │ JSON Result (Malicious/OK)  │                              │
│        └────────────┬────────────────┘                              │
│                     ▼                                               │
│        ┌─────────────────────────────┐                              │
│        │ Result Dispatcher           │───▶  Flask API → Dashboard   │
│        └─────────────────────────────┘                              │
│                                                                      │
├──────────────────────────────────────────────────────────────────────┤
│                     Optional NVIDIA Morpheus Pipeline                │
│                                                                      │
│   ┌────────────────────────────┐    ┌────────────────────────────┐   │
│   │ Triton Inference Server    │    │ Morpheus Streaming Modules │   │
│   │ GPU-based Parallel Inference│◄──► Data Loader & Preprocessor │   │
│   └────────────────────────────┘    └────────────────────────────┘   │
└──────────────────────────────────────────────────────────────────────┘


**📌 Component Summary:**

## 🧠 Core Analysis Logic:

Watchdog: Monitors log directories.

Scapy: Captures live packets.

Parsers: Extract relevant structured data.

Sliding Context Manager: Maintains N-shot learning memory.

LLM Module: Interacts with DeepSeek via LM Studio (OpenAI-compatible API).

Result Dispatcher: Publishes JSON results.

## 🌐 UI:

Flask Web Dashboard: Fetches and displays logs, memory context, inference results with threat alerts.

⚙️ Future Integration:
Triton Inference Server + Morpheus: Adds GPU acceleration pipeline for scaling and streaming.

---

## 🧰 Minimum System Requirements

- **CPU:** Ryzen 7 4800H or equivalent
- **GPU:** NVIDIA RTX 3050 (4GB VRAM)
- **RAM:** 16 GB DDR4 (3200 MT/s)
- **OS:** Linux/Windows (Docker enabled)

---

## 🛠️ How to Run

### 1. Clone the Repo
```bash
git clone https://github.com/YOUR_USERNAME/deepseek-morpheus-analyzer.git
cd deepseek-morpheus-analyzer
```

### 2. Start LM Studio
- Load the DeepSeek model
- Enable OpenAI-compatible API on port `1234`

### 3. Local (No Docker)
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```

Dashboard:
```bash
cd dashboard
python app.py
```

Access: `http://localhost:5000`

### 4. Full Dockerized Stack
```bash
docker-compose up --build
```

---

## 📊 Dashboard Preview
- **Auto-refresh every 2 seconds**
- **Red background** for malicious results
- **Sorted by time** with memory context display

---

## 📈 Morpheus & Triton Integration
- Triton server listens on ports `8000`, `8001`, and `8002`
- Placeholder for Morpheus streaming pipeline for future GPU-based LLM evaluation

---

## 🤝 Connect

![LinkedIn](https://www.linkedin.com/in/swapneel-ghosh-834851218/)

If this project helped you, give it a ⭐ and share your ideas through Issues or PRs!

