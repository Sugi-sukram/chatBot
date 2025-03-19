from sqlalchemy.orm import Session
from app.models.chat_history import ChatHistory
from app.schemas.chat_history import ChatHistoryCreate, ChatHistoryResponse
from fastapi import HTTPException

def create(db: Session, request: ChatHistoryCreate) -> ChatHistoryResponse:
    chat_record = ChatHistory(
        user_id=request.user_id,
        message=request.message,
        response=request.response
    )
    db.add(chat_record)
    db.commit()
    db.refresh(chat_record)
    return ChatHistoryResponse(
        id=chat_record.id,
        user_id=chat_record.user_id,
        message=chat_record.message,
        response=chat_record.response,
        timestamp=chat_record.timestamp
    )

def get(db: Session, user_id: int) -> list[ChatHistoryResponse]:
    chat_records = db.query(ChatHistory).filter(ChatHistory.user_id == user_id).all()
    return [
        ChatHistoryResponse(
            id=record.id,
            user_id=record.user_id,
            message=record.message,
            response=record.response,
            timestamp=record.timestamp
        )
        for record in chat_records
    ]
