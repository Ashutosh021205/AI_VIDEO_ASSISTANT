# 🎬 AI Video Assistant

An AI-powered video processing system that converts videos (YouTube or local files) into **transcripts, summaries, and structured insights** using a GenAI pipeline.

---

## 🚀 Features

- 🎥 Supports YouTube URLs and local video files  
- 🔊 Audio extraction from video  
- 🧠 Automatic speech-to-text transcription  
- ✍️ AI-powered summarization of content  
- 📌 Key points, decisions, and action item extraction  
- 🔎 RAG-style question answering over video content  
- 🌐 Multi-language support (e.g., English, Hinglish)  

---

## 🧠 System Workflow

The project follows a **GenAI pipeline for video intelligence**:

1. **Input Video Source**
   - YouTube URL or local video file  

2. **Audio Extraction**
   - Extract audio from video using processing utilities  

3. **Transcription Layer**
   - Convert speech → text using ASR (Automatic Speech Recognition)  

4. **AI Processing Layer**
   - Summarization of transcript  
   - Extraction of:
     - Key points  
     - Action items  
     - Important decisions  
     - Questions  

5. **RAG-Based Q&A Engine**
   - Users can query the video content using LLM-based retrieval over transcript  

---

## 🛠️ Tech Stack

- Python  
- yt-dlp (YouTube video download)  
- pydub (audio processing)  
- Speech-to-Text (Whisper / ASR models)  
- Large Language Models (LLMs)  
- Prompt Engineering  
- RAG (Retrieval-Augmented Generation)  
- Streamlit (optional UI)  
- FFmpeg (audio/video processing backend)

---
## 📂 Project Structure

├── main.py # Entry point
├── core/
│ ├── transcriber.py # Speech-to-text module
│ ├── summarizer.py # AI summarization logic
│ ├── extractor.py # Key info extraction (action items, decisions)
│ ├── rag_engine.py # Q&A over transcript
├── utils/
│ ├── audio_processor.py # Video/audio handling
├── runtime.txt # Environment setup
├── requirements.txt
└── README.md


---

## ⚙️ How It Works

1. User provides a **YouTube link or local video file**
2. System extracts audio using `yt-dlp` or local processing
3. Audio is converted into text using transcription engine
4. LLM processes transcript to:
   - Summarize content  
   - Extract key insights  
   - Identify action items and decisions  
5. A **RAG-based engine** allows querying the video content like a chatbot  

---

## 📂 Project Structure
