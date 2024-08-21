from sqlalchemy.orm import Session

from datetime import datetime, timedelta, timezone
from typing import Annotated

import jwt
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jwt.exceptions import InvalidTokenError
from passlib.context import CryptContext
from pydantic import BaseModel

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Tạo đối tượng pwd_context để thực hiện hash mật khẩu và xác thực mật khẩu
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Tạo đối tượng để thực hiện việc tách token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# Xác thực mật khẩu ban đầu với mật khẩu đã hash
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)



#====================== 1.1. Xác thực email và password
def authenticate_user(db: Session, email: str, password: str):
    user = crud.get_user_by_email(db, email)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

#====================== 1.2. Tạo mã jwt
def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()                                                             # thông tin cần mã hóa jwt
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta                              
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)                     # nếu thời gian hết hạn token không được cung cấp thì mặc đinh thời gian hết hạn là 15 phút
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)                # mã hóa jwt
    return encoded_jwt


# Đăng ký user
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

# Đăng nhập
@app.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Session = Depends(get_db)
) -> schemas.Token:
    user = authenticate_user(db, email = form_data.username, password = form_data.password)       # xác thực username và password
    if not user:                                                                          # nếu không tìm được user thỏa mãn trả về lỗi
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)                 # Tạo time hết hạn token
    access_token = create_access_token(                                                   # Tạo token
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return schemas.Token(access_token=access_token, token_type="bearer")



