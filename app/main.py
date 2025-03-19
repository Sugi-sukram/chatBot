from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes import user, chat_bot ,user_interface,chat_histories
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

# Include Routers
app.include_router(user_interface.router, prefix="")
app.include_router(user.router, prefix="/auth")
app.include_router(chat_bot.router, prefix="/chatbot")
app.include_router(chat_histories.router, prefix="")