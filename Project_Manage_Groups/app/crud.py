from sqlalchemy.orm import Session
from passlib.context import CryptContext
from . import models, schemas

# Tạo đối tượng pwd_context để thực hiện hash mật khẩu 
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Hash mật khẩu
def get_password_hash(password):
    return pwd_context.hash(password)

# đọc dữ liệu
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

# tạo tài khoản mới
def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password) 
    db_user = models.User(email=user.email, user_name =user.user_name, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user