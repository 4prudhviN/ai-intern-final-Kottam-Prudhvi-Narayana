<p align="center">
  <img src="assets/logo.png" width="140">
</p>

<h1 align="center">
AI Research Intelligence Platform
</h1>

![Python](https://img.shields.io/badge/Python-3.11+-blue?style=flat-square&logo=python)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-FF4B4B?style=flat-square&logo=streamlit)
![Groq](https://img.shields.io/badge/AI-Groq%20Llama%203.3-orange?style=flat-square)
![MCP](https://img.shields.io/badge/Storage-MCP%20File%20System-green?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-lightgrey?style=flat-square)

A professional, enterprise-grade AI research platform powered by a multi-agent pipeline. Generates structured intelligence reports with source attribution, analytics, and professional PDF/TXT export.

---

## 🏗️ Architecture

```
User Input
    ↓
Streamlit Dashboard  (premium dark UI)
    ↓
Input Validation     (empty/length checks)
    ↓
Research Agent       (deep analysis)
    ↓
Trend Analysis Agent (market outlook)
    ↓
Executive Summary Agent (synthesis)
    ↓
MCP File System Layer  (persistence)
    ↓
Export Engine        (PDF + TXT)
```

---

## 🌟 Features

| Feature | Description |
|---|---|
| **Multi-Agent Pipeline** | Research → Trend → Summary agents run in sequence |
| **5 Research Modes** | Business, Technical, Startup, Investor, Academic |
| **Depth Control** | 1–10 slider for brief overviews to deep dossiers |
| **Streaming Output** | Word-by-word real-time text rendering |
| **Pipeline Trace** | Live AI orchestration visualization |
| **Research Analytics** | Word count, read time, mode tracking |
| **Source Attribution** | Structured reference citations per report |
| **Export Engine** | Styled PDF with headers/footers + TXT |
| **Research Vault** | Persistent history via MCP File System |
| **Error Handling** | Graceful API failure and empty-input screens |

---

## 🚀 Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure API key** — create `.env`:
   ```env
   GROQ_API_KEY=your_groq_key_here
   ```
   Get your free key at [console.groq.com](https://console.groq.com)

3. **Run the platform:**
   ```bash
   python -m streamlit run app.py
   ```

---

## 📁 Project Structure

```
ai-intern-final/
├── app.py                    # Main Streamlit dashboard
├── services/
│   ├── groq_service.py       # Groq AI inference client
│   ├── agent_pipeline.py     # Multi-agent orchestration
│   ├── mcp_client.py         # MCP File System layer
│   └── export_service.py     # PDF + TXT generation
├── utils/
│   ├── validators.py         # Input validation
│   └── helpers.py            # Timestamps etc.
├── assets/
│   └── style.css             # Premium dark theme
├── data/
│   └── research_history.json # Persistent report vault
├── logs/
│   └── app.log               # System audit trail
└── exports/                  # Generated PDF/TXT files
```

---

## 🗺️ Future Roadmap

- [ ] RAG pipeline with vector database (Pinecone/Chroma)
- [ ] Multi-modal document analysis (PDF/image upload)
- [ ] LangGraph stateful agent orchestration
- [ ] Live financial data API integration
- [ ] User authentication and team workspaces

---

*Developed for the AI Intern Final Evaluation — showcasing agentic design and professional AI engineering.*
