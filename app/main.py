from fastapi import FastAPI
from app.routes import user as user_routes
from app.db.session import Base, engine
from app.models.chat_history import ChatHistory  # ✅ Import ChatHistory
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Create tables
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

# Include routes
app.include_router(user_routes.router)
