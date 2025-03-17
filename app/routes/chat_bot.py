# app/routes/chat_bot.py

from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
import google.generativeai as genai

chat_bot = APIRouter()  # ✅ Correctly defining the router

templates = Jinja2Templates(directory="templates")

API_KEY = "AIzaSyB4_Hb_BNXCHKkDssGQU0I0Gblm6xHX3_Y"

if API_KEY != "YOUR_API_KEY":
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel("gemini-1.5-flash")
else:
    print("Please replace 'YOUR_API_KEY' with your actual API key.")

system_prompt = (
    "You are a helpful assistant. Please answer only medical-related questions. "
    "If the user asks a question on another topic, respond with: "
    "'I am sorry, I can't answer this question, I can only answer for medical-related questions. "
    "Please ask questions in this topic.' Please answer concisely and accurately."
)

chat_history = [{"role": "user", "parts": system_prompt}]

@chat_bot.post("/chat")
async def chat(request: Request):
    try:
        data = await request.json()
        user_input = data.get("message")

        if not user_input:
            raise HTTPException(status_code=400, detail="Message is required.")

        chat_history.append({"role": "user", "parts": user_input})

        chat = model.start_chat(history=chat_history)
        response = chat.send_message(user_input)
        model_response = response.text

        chat_history.append({"role": "model", "parts": model_response})

        return JSONResponse(content={"response": model_response})

    except Exception as e:
        print(f"Error generating response: {e}")
        raise HTTPException(status_code=500, detail=str(e))
