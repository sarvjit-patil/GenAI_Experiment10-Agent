---
title: GenAI Experiment 10 Agent
emoji: 🤖
colorFrom: blue
colorTo: purple
sdk: docker
app_port: 7860
---

<div align="center">

# 🔎 AI Research Agent

### _Search the web. Summarize with AI. Get answers in seconds._

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-UI-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Google Gemini](https://img.shields.io/badge/Google%20Gemini-2.5--flash-4285F4?logo=google&logoColor=white)](https://ai.google.dev/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker&logoColor=white)](https://www.docker.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

<br/>

<img src="https://img.icons8.com/color/96/artificial-intelligence.png" alt="AI Agent" width="96"/>

**A Generative AI–powered research agent that searches the web using DuckDuckGo, then distills the results into a concise 3-bullet research brief using Google Gemini — all through a clean Streamlit interface.**

---

[Features](#-features) •
[Architecture](#-architecture) •
[Quick Start](#-quick-start) •
[Docker](#-docker-deployment) •
[Testing](#-testing) •
[Tech Stack](#-tech-stack)

</div>

---

## ✨ Features

| Feature | Description |
|---|---|
| 🌐 **Web Search** | Multi-query search via DuckDuckGo with automatic deduplication (up to 10 unique results) |
| 🧠 **AI Summarization** | LLM-powered summarization using Google Gemini 2.5 Flash via LangChain |
| 📋 **Structured Output** | Always returns exactly 3 concise bullet points — no fluff |
| ✅ **Input Validation** | Robust topic validation and error handling throughout the pipeline |
| 🖥️ **Streamlit UI** | Clean, centered web interface with real-time progress feedback |
| 🐳 **Docker Support** | Production-ready Dockerfile for easy containerized deployment |
| 🧪 **Unit Tests** | Pytest-based test suite covering core utility functions |

---

## 🏗️ Architecture

```
User Input (Topic)
       │
       ▼
┌─────────────────────┐
│   Streamlit UI      │   ← app.py
│   (Frontend)        │
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│  Research Agent      │   ← agent.py
│  Pipeline            │
│                      │
│  1. validate_topic() │   → Sanitize & validate input
│  2. search_web()     │   → DuckDuckGo (3 query variants)
│  3. summarize()      │   → Google Gemini 2.5 Flash
│  4. format_bullets() │   → Enforce 3-bullet structure
└─────────────────────┘
         │
         ▼
   3-Bullet Research Brief
```

---

## 🚀 Quick Start

### Prerequisites

- **Python 3.11+**
- A **Google Gemini API key** — [get one free](https://aistudio.google.com/apikey)

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/Experiment10-Agent.git
cd Experiment10-Agent
```

### 2. Create a virtual environment

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

### 5. Run the app

```bash
streamlit run app.py
```

The app will open at **http://localhost:8501** 🎉

---

## 🐳 Docker Deployment

```bash
# Build the image
docker build -t ai-research-agent .

# Run the container
docker run -p 7860:7860 --env-file .env ai-research-agent
```

Access the app at **http://localhost:7860**

---

## 🧪 Testing

```bash
pytest tests/ -v
```

Tests cover:
- ✅ Topic validation (valid input, empty/whitespace input)
- ✅ Bullet formatting (exactly 3 bullets enforced)
- ✅ Edge-case error handling

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| [Streamlit](https://streamlit.io/) | Web UI framework |
| [LangChain](https://www.langchain.com/) | LLM orchestration & prompt templating |
| [Google Gemini 2.5 Flash](https://ai.google.dev/) | Large language model for summarization |
| [DuckDuckGo Search](https://pypi.org/project/duckduckgo-search/) | Privacy-friendly web search API |
| [python-dotenv](https://pypi.org/project/python-dotenv/) | Environment variable management |
| [pytest](https://docs.pytest.org/) | Unit testing framework |
| [Docker](https://www.docker.com/) | Containerization |

---

## 📁 Project Structure

```
Experiment10-Agent/
├── agent.py              # Core research agent (search + summarize + format)
├── app.py                # Streamlit web application
├── requirements.txt      # Python dependencies
├── Dockerfile            # Container configuration
├── .env                  # API keys (not committed)
├── .gitignore            # Git ignore rules
├── tests/
│   └── test_agent.py     # Unit tests
└── .github/
    └── workflows/
        └── ci-cd.yml     # CI/CD pipeline
```

---

## 📄 License

This project is part of the **B.Tech Final Year — Generative AI Experiments** coursework.

---

<div align="center">

**Built with ❤️ using Google Gemini & LangChain**

</div>
