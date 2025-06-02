# 🧠 AutoWorkflow AI

**AutoWorkflow AI** is an intelligent task automation platform powered by AI agents. Using CrewAI + FastAPI, it converts natural language prompts into actionable workflows using Gmail, Notion, Sheets, and more.

## 🚀 Features
- 📧 Send emails automatically using Gmail API
- 📅 Fetch calendar events & send WhatsApp reminders
- 📊 Update Google Sheets with summaries, task logs
- 🧠 Agent orchestration with CrewAI
- 🔐 Auth system with user tasks & logs

## 🔧 Tech Stack

| Layer            | Tools Used                                      |
|------------------|--------------------------------------------------|
| LLM + Agents     | CrewAI / LangGraph + OpenAI/Gemini               |
| Backend          | FastAPI / Flask                                  |
| Database         | PostgreSQL / MongoDB                             |
| APIs Integrated  | Gmail, Notion, Google Calendar, Sheets, Twilio   |
| Frontend (Opt.)  | Streamlit or React                               |
| Deployment       | Replit, Render, Fly.io, UptimeRobot              |

## 📂 Architecture

[Frontend UI] ──▶ [FastAPI Backend]
│
├──▶ [CrewAI Agent Orchestration]
│ ├── Gmail Sender
│ ├── Calendar Fetcher
│ ├── Notion Logger
│ └── Sheet Updater
│
└──▶ [Postgres DB]

yaml
Copy
Edit

## 🗓️ Milestones
- Week 1: Backend + DB + simple agent
- Week 2: Gmail & Notion tools
- Week 3: Auth + scheduler + optional UI
- Week 4: Finalize, demo, polish GitHub

## 📽️ Demo
*Coming soon – short video demo here*

---

## 🧠 Why This Project?
This repo showcases system design, agent pipeline, and real-world AI integration — perfect for internships and demonstrating applied AI skills.

## 📜 License
MIT License
