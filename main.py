from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
import os
from dotenv import load_dotenv
import ssl
import certifi
import time
import requests
import uvicorn

SYSTEM_PROMPT = """
You are an elite senior frontend engineer and UI/UX designer at a top-tier product company.

Your task is to generate HIGH-END, visually stunning, production-grade landing pages.

Design standards:
- Equivalent to Stripe, Linear, Apple, Vercel level quality
- Modern, aesthetic, polished UI with strong visual hierarchy
- Use spacing, typography, gradients, shadows effectively
- The design must NOT look basic or generic

STRICT REQUIREMENTS:

1. Output ONLY a full HTML file (no explanations)

2. Use:
- Advanced CSS (gradients, glassmorphism, shadows, blur effects)
- CSS variables for theme
- Flexbox and Grid layout
- Responsive design (mobile-first)

3. Visual Design:
- Use a modern color palette (dark mode preferred)
- Include gradient accents
- Gradient UI
- Smooth hover animations
- Card-based layouts
- Subtle shadows and depth
- Proper spacing and alignment

4. Animations:
- Fade-in / slide-up on load
- Hover transitions
- Micro-interactions on buttons/cards

5. UI Sections (must be well designed):
- Navbar (sticky, modern)
- Hero section (bold headline + CTA + visual emphasis)
- Features section (cards with icons)
- About section (clean layout)
- Testimonials or social proof section
- Contact section (modern form UI)
- Footer (minimal, structured)

6. Content:
- Use realistic startup/product-style content
- Do NOT leave placeholder lorem ipsum

7. JavaScript:
- Add interactivity:
  - Mobile menu toggle
  - Scroll effects
  - Button interactions

8. Quality Bar:
- The UI must look like a real high-end, production-grade SaaS product landing page
- Avoid plain/basic layouts
- Avoid default HTML styling
- Avoid minimal or unstyled components

Return ONLY the complete HTML file with inline CSS and JS.
"""

# Fix SSL issue (important on Windows)
ssl._create_default_https_context = ssl.create_default_context(cafile=certifi.where())

load_dotenv()

app = FastAPI()

HF_TOKEN = os.getenv("HF_TOKEN")

API_URL = "https://router.huggingface.co/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {HF_TOKEN}",
    "Content-Type" : "application/json"
}


# Request schema
class GenerateRequest(BaseModel):
    prompt: str

# Serve frontend
@app.get("/")
async def serve_home():
    return FileResponse("templates/index.html")

def query_huggingface(user_prompt):

    payload = {
        "model": "Qwen/Qwen2.5-Coder-7B-Instruct",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 2000
    }

    for _ in range(3):
        response = requests.post(API_URL, headers=headers, json=payload)

        if response.status_code == 503:
            print("Model loading... retrying in 5s")
            time.sleep(5)
            continue

        if response.status_code == 200:
            return response.json()

        raise Exception(response.text)

    raise Exception("Model is still loading after retries")

# Generate website
@app.post("/generate")
async def generate_website(req: GenerateRequest):
    try:
        result = query_huggingface(req.prompt)

        # ✅ Correct parsing
        generated_text = result["choices"][0]["message"]["content"]

        html = generated_text.replace("```html", "").replace("```", "").strip()

        return {
            "html": html,
            "tokens_used": len(html) // 4
        }

    except Exception as e:
        return {
            "html": f"<h1>Error</h1><p>{str(e)}</p>",
            "tokens_used": 0
        }
    
port = int(os.environ.get("PORT", 10000))

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=port)
