#  Create Your Website AI

 Generate stunning, production-ready websites using AI — from just a simple prompt.

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

## 🔌 2. API Endpoint Documentation

### 🔹 Base URL
```
https://<your-app>.onrender.com
```

---

### 🔹 Generate Website

**POST /generate**

#### Request
```json
{
  "prompt": "Create a modern portfolio website",
  "style": "modern",
  "pages": 2
}
```

#### Response
```json
{
  "status": "success",
  "files": {
    "index.html": "<html>...</html>",
    "style.css": "body {...}",
    "script.js": "// JS code"
  }
}
```

---

### 🔹 Health Check

**GET /health**

```json
{
  "status": "ok"
}
```

---

## 🤖 3. Model Selection & Integration Rationale

### 🔹 Why LLMs?
- Convert natural language → code
- Reduce manual development effort
- Enable rapid prototyping

---

### 🔹 Selection Criteria

| Criteria | Description |
|---------|------------|
| Accuracy | Valid code generation |
| Speed | Fast API response |
| Cost | Efficient usage |
| Flexibility | Multiple styles |

---

### 🔹 Integration Flow

```
User Input → FastAPI → LLM API → Generated Code → Response
```

---

### 🔹 Prompt Strategy
- Structured prompts for layout + style
- Ensures clean HTML/CSS separation

---

## 🚀 4. Deployment & Setup Instructions (Render)

### 🔹 Prerequisites
- GitHub repository
- Render account
- API key

---

### 🔹 Step 1: Clone Repository
```bash
git clone https://github.com/sdShaggy/Create-Your-Website-AI.git
cd Create-Your-Website-AI
```

---

### 🔹 Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

---

### 🔹 Step 3: Environment Variables

Create `.env`:
```
OPENAI_API_KEY=your_api_key
```

---

### 🔹 Step 4: Run Locally
```bash
uvicorn main:app --reload
```

---

### 🔹 Step 5: Deploy on Render

Configuration:

| Setting | Value |
|--------|------|
| Build Command | pip install -r requirements.txt |
| Start Command | uvicorn main:app --host 0.0.0.0 --port 10000 |

---

### 🔹 Step 6: Test API

```bash
curl -X POST https://your-app.onrender.com/generate -H "Content-Type: application/json" -d '{"prompt":"Create a business website"}'
```

---

## 📂 5. Project Structure

```
├── main.py
├── requirements.txt
├── .env
├── static/
├── templates/
└── README.md
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
- LLM APIs
- HTML/CSS/JS
- Render

---

## 📜 License

MIT License

---

## 💡 Author

Sarvagya Dwivedi

---

## ⭐ Support

Star ⭐ this repo if you like it!
