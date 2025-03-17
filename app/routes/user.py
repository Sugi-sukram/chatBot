from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserResponse,LoginRequest
from app.crud import user as crud_user
from app.crud.user import authenticate_user as authenticate
from app.db.session import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/signUp/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(crud_user.User).filter(crud_user.User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud_user.create_user(db=db, user=user)

@router.get("/users/{user_id}", response_model=UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud_user.get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.post("/login/")
def login(login_data: LoginRequest, db: Session = Depends(get_db)):
    user = authenticate(db, login_data.email, login_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid email or password")
    return {"message": "User authenticated successfully"}

