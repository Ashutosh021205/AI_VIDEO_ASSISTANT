# 📝 AI Meeting Summarizer

An AI-powered Meeting Intelligence Platform that automatically converts meeting audio/video into **accurate transcripts, structured summaries, key decisions, action items, and intelligent meeting insights** using **Whisper, LangChain, Mistral AI, and Retrieval-Augmented Generation (RAG).**

---

## 🚀 Features

- 🎙️ Supports Meeting Audio, Video Files, and YouTube URLs
- 🔊 Automatic Audio Processing
- 📝 Speech-to-Text Transcription using Whisper
- 🤖 AI-Powered Meeting Summarization
- 📌 Automatic Meeting Title Generation
- ✅ Action Item Extraction
- 🔑 Key Decision Identification
- ⚠️ Open Questions & Follow-up Detection
- 💬 Ask Questions About Your Meeting (RAG)
- 🌍 Multi-language Support (English & Hinglish)
- 🖥️ Interactive Streamlit Dashboard

---

# 🧠 System Workflow

The project follows an end-to-end GenAI pipeline for meeting intelligence.

```text
Meeting Audio / Video
           │
           ▼
Audio Processing
           │
           ▼
Speech-to-Text (Whisper)
           │
           ▼
Meeting Transcript
           │
           ▼
LLM (Mistral AI)
           │
           ├──────────────┐
           │              │
           ▼              ▼
Meeting Summary      Meeting Title
           │
           ├──────────────┐
           │              │
           ▼              ▼
Action Items     Key Decisions
           │
           ▼
Open Questions / Risks
           │
           ▼
RAG Knowledge Base
           │
           ▼
Ask Questions About Meeting
```

---

# ✨ Features Explained

### 🎙️ Speech-to-Text

- Converts meeting recordings into accurate transcripts using Whisper.
- Supports long meetings through chunked transcription.

---

### 📝 AI Meeting Summary

Automatically generates a concise meeting summary highlighting:

- Main discussion points
- Important outcomes
- Overall meeting context

---

### 📌 Meeting Title

Generates a professional meeting title automatically.

Example:

- Sprint Planning Meeting
- Weekly Sales Review
- Product Launch Discussion

---

### ✅ Action Item Extraction

Identifies:

- Task
- Owner
- Deadline
- Priority

Example:

| Owner | Task | Deadline | Priority |
|-------|--------|-----------|----------|
| Rahul | Update API | Friday | High |
| Priya | Prepare Presentation | Monday | Medium |

---

### 🔑 Key Decisions

Automatically extracts all finalized decisions discussed during the meeting.

---

### ⚠ Open Questions

Detects:

- Pending discussions
- Unresolved issues
- Risks
- Follow-up topics

---

### 💬 Chat with Your Meeting

Uses Retrieval-Augmented Generation (RAG) so users can ask questions like:

- What did Rahul commit to?
- What is the project deadline?
- Who is responsible for deployment?
- What were the final decisions?

---

# 🛠 Tech Stack

## Languages

- Python

## AI / LLM

- Mistral AI
- LangChain
- Prompt Engineering

## Speech Recognition

- OpenAI Whisper

## Vector Database

- ChromaDB

## Audio Processing

- FFmpeg
- Pydub
- yt-dlp

## Frontend

- Streamlit

## Retrieval

- Retrieval-Augmented Generation (RAG)

---

# 📂 Project Structure

```
AI_MEETING_SUMMARIZER
│
├── app.py                      # Streamlit UI
├── main.py                     # Main Pipeline
│
├── core/
│   ├── transcriber.py          # Whisper Speech-to-Text
│   ├── summarizer.py           # Meeting Summary & Title
│   ├── extractor.py            # Action Items, Decisions, Open Questions
│   ├── rag_engine.py           # RAG-based Meeting Chat
│   ├── vector_store.py         # Chroma Vector Store
│
├── utils/
│   ├── audio_processor.py      # Audio & Video Processing
│
├── requirements.txt
├── runtime.txt
├── README.md
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/Ashutosh021205/AI_VIDEO_ASSISTANT.git
```

Navigate to the project

```bash
cd AI_VIDEO_ASSISTANT
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
MISTRAL_API_KEY=YOUR_API_KEY
```

Run the application

```bash
streamlit run app.py
```

---

# 🚀 How It Works

1. Upload a meeting audio/video or provide a YouTube URL.
2. Audio is extracted and preprocessed.
3. Whisper converts speech into text.
4. Mistral AI generates:
   - Meeting Title
   - Meeting Summary
   - Action Items
   - Key Decisions
   - Open Questions
5. Transcript is indexed into ChromaDB.
6. Users can ask questions using the RAG-powered assistant.

---

# 📸 Application Output

The application provides:

- 📝 Meeting Title
- 📋 Meeting Summary
- ✅ Action Items
- 🔑 Key Decisions
- ⚠ Open Questions
- 📄 Full Transcript
- 💬 Chat with Meeting

---

# 🎯 Future Enhancements

- 📄 Export Meeting Report as PDF
- 📥 Download Transcript
- 📊 Meeting Analytics Dashboard
- 👥 Speaker Diarization
- 🌍 Automatic Language Detection
- ☁ Cloud Deployment
- 🗂 Meeting History Database

---

# 📈 Use Cases

- Corporate Meetings
- Daily Standups
- Client Calls
- Team Discussions
- Project Planning
- Online Lectures
- Interview Recordings

---

# 👨‍💻 Author

**Ashutosh Kunjeer**

- LinkedIn: https://www.linkedin.com/in/ashutosh-kunjeer
- GitHub: https://github.com/Ashutosh021205

---

# ⭐ If you found this project useful, don't forget to star the repository!
