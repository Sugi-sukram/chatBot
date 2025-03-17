from fastapi import APIRouter, Request
from app.crud.bot import chatbot


router = APIRouter()

@router.post("/")
async def chat(request: Request):
    return await chatbot(request)
