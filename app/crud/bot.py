# app/routes/bot_response.py

from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
import google.generativeai as genai

API_KEY = "AIzaSyB4_Hb_BNXCHKkDssGQU0I0Gblm6xHX3_Y"

if API_KEY == "YOUR_API_KEY":
    raise ValueError("Please replace 'YOUR_API_KEY' with your actual API key.")

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

system_prompt = (
    "You are a helpful assistant. Please answer only medical-related questions. "
    "If the user asks a question on another topic, respond with: "
    "'I am sorry, I can't answer this question, I can only answer for medical-related questions. "
    "Please ask questions in this topic.'"
)

chat_history = [{"role": "user", "parts": system_prompt}]

async def chatbot(request: Request):
    try:
        data = await request.json()
        user_input = data.get("message")

        if not user_input:
            raise HTTPException(status_code=400, detail="Message is required.")

        chat_history.append({"role": "user", "parts": user_input})
        response = model.start_chat(history=chat_history).send_message(user_input).text
        chat_history.append({"role": "model", "parts": response})

        return JSONResponse(content={"response": response})

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
