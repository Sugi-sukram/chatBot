from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.controller import chat_history
from app.database.session import SessionLocal
from app.schemas.user import UserCreate
from app.schemas.chat_history import ChatHistoryCreate, ChatHistoryResponse

router = APIRouter()

# Dependency to get the DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# GET request to retrieve chat history by user_id
@router.get("/histories/{user_id}")
def get_chat_histories(user_id: int, db: Session = Depends(get_db)):
    return chat_history.get(db, user_id)

# POST request to create a chat history record
@router.post("/histories", response_model=ChatHistoryResponse)
def create_chat_history(request: ChatHistoryCreate, db: Session = Depends(get_db)):
    return chat_history.create(db, request)
