from pydantic import BaseModel
from datetime import datetime

class ChatHistoryBase(BaseModel):
    user_id: int
    message: str
    response: str

class ChatHistoryCreate(ChatHistoryBase):  # ✅ Correct structure
    pass  # No extra fields

class ChatHistoryResponse(ChatHistoryBase):
    id: int
    timestamp: datetime

    class Config:
        from_attributes = True  # ✅ Ensure ORM compatibility
