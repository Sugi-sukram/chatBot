from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse  # Import FileResponse
from app.routes import user, chat_bot
from app.database.session import Base, engine
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount Static Files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Create Tables
Base.metadata.create_all(bind=engine)

# Root Route
@app.get("/")
def read_root():
    return FileResponse("static/login.html")

# Signup Route
@app.get("/signup")
def read_signup():
    return FileResponse("static/signup.html")

# Chatbot Route (Static HTML)
@app.get("/chatbot-page")
def read_chatbot():
    return FileResponse("static/chatbot.html")

# Include Routers
app.include_router(user.router, prefix="/auth")
app.include_router(chat_bot.router, prefix="/chatbot")
