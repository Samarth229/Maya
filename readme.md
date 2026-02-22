# Maya — Offline AI Companion

Maya is a personal AI companion designed for emotionally aware, long-term interaction.  
Built as a modular, scalable system with hybrid intelligence and full offline capability.

---

## Current Capabilities (v1.1)

- Fully offline AI (powered by local LLM via Ollama)
- Voice + Text interaction modes
- Wake-word based activation ("maya")
- Persistent user memory (profile + conversation history)
- Emotion-aware response system
- Emotion continuity within session
- Hybrid intelligence (rule-based + ML-based detection)
- Automatic online/offline decision engine (future-ready architecture)

---

## Core Architecture

- Modular design (`core/`, `online/`, `data/`)
- Emotion & intent detection engine
- Emotional memory with trend tracking
- Hybrid response prioritization (emotion-first logic)
- Local LLM integration via Ollama
- Scalable foundation for future personality modeling & adaptive gameplay

---

## Known Limitations (v1.1)

- Proper noun recognition (e.g., user names) may be imperfect due to offline STT limitations
- Wake-word detection is keyword-based (not ML-trained yet)
- Offline speech-to-text introduces slight latency
- Emotional responses are rule-prioritized (adaptive personality under development)

---

## Project Vision

Maya is being developed as a long-term AI companion —  
not just a chatbot, but an emotionally aware system capable of:

- Behavioral adaptation  
- Conversation continuity across sessions  
- Personalized interaction memory  
- Future interactive gameplay integration  

---

## Tech Stack

- Python 3.14  
- Ollama (Local LLM)  
- Vosk (Offline STT)  
- Modular architecture design  
