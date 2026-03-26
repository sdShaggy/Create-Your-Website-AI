#  Create Your Website AI

 Prototype V 0.1

 
 Generate stunning, production-ready websites using AI — from just a simple prompt.

---

## 🌐 Live Demo

🚀 Try the app here:  
👉 https://create-your-website-ai.onrender.com/

---

# 📘 Technical Documentation

## 🏗️ 1. System Architecture & Component Overview

### 🔹 High-Level Architecture

```
User (Frontend UI)
        ↓
FastAPI Backend (API Layer)
        ↓
AI Model (LLM / Prompt Engine)
        ↓
Website Generator Engine
        ↓
HTML/CSS/JS Output
        ↓
Deployment (Render)
```

---

### 🔹 Components Breakdown

#### 1. Frontend Layer
- Built using HTML, CSS, JavaScript
- Accepts user prompts
- Sends API requests
- Displays generated website

---

#### 2. Backend Layer (FastAPI)
- Handles API endpoints
- Processes user input
- Sends prompt to AI model
- Returns structured website code

---

#### 3. AI Model Layer
- Uses LLM APIs (Qwen)
- Converts natural language into:
  - HTML structure
  - CSS styling
  - JavaScript logic

---

#### 4. Website Generator Engine
- Cleans AI output
- Ensures valid HTML/CSS
- Structures files properly

---

#### 5. Deployment Layer
- Hosted on Render
- Can serve static files or API

---

## 🤖 3. Model Selection & Integration Rationale

### 🔹 Why LLMs?
- Convert natural language → code
- Reduce manual development effort
- Enable rapid prototyping

---


### 🔹 Integration Flow

```
User Input → FastAPI → LLM API → Generated Code → Response
```

---

## ⚙️ 6. Future Improvements

- Database integration
- Authentication
- Multi-page support
- Live preview
- One-click deploy

---

## 🧠 Tech Stack

- FastAPI
- LLM APIs (Qwen2.5-coder-7B-Instruct)
- HuggingFace
- HTML/CSS/JS
- Render
- MongoDB
- HTML + CSS + JS

---

## 💡 Author

Made by Sarvagya Dwivedi towards personal learning initiatives
