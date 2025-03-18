from fastapi import APIRouter
from fastapi.responses import FileResponse

router = APIRouter()

# Root Route (Login Page)
@router.get("/")
def read_root():
    return FileResponse("static/login.html")

# Signup Route
@router.get("/signup")
def read_signup():
    return FileResponse("static/signup.html")

# Chatbot Page Route
@router.get("/chatbot-page")
def read_chatbot():
    return FileResponse("static/chatbot.html")
