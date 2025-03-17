from pydantic import BaseModel
from datetime import datetime

class ChatHistoryBase(BaseModel):
    message: str
    response: str

class ChatHistoryCreate(ChatHistoryBase):
    user_id: int

class ChatHistoryResponse(ChatHistoryBase):
    id: int
    user_id: int
    timestamp: datetime

    class Config:
        from_attributes = True