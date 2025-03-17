# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from app.schemas.user import UserCreate, UserResponse,LoginRequest
# from app.crud import user as crud_user
# from app.crud.user import authenticate_user as authenticate
# from app.database.session import SessionLocal

# router = APIRouter()

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @app.route("/")
# def index():
#     return render_template("index.html")
        

# @router.post("/chat/", response_model=UserResponse)
# def create_user(user: UserCreate, db: Session = Depends(get_db)):
#     existing_user = db.query(crud_user.User).filter(crud_user.User.email == user.email).first()
#     if existing_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return crud_user.create_user(db=db, user=user)
