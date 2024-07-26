from sqlalchemy.orm import Session

from . import models, schemas

# đọc dữ liệu
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()
# lấy 100 user vị trí từ (skip + 1) đến (limit) và trả về dưới dạng danh sách

# tạo dữ liệu
def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# đọc dữ liệu
def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()

# tạo dữ liệu
def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# **item.dict()có tác dụng unpack tất cả các cặp key-value trong dict thành key = value
# db_item = models.Item(**item.dict(), owner_id=user_id) tạo 1 đối tượng của bảng Item với các thuộc tính
#     title=item.title,
#     description=item.description,
#     owner_id=user_id
#Lệnh db.refresh(db_item) giúp đảm bảo rằng đối tượng db_item trong Python có các giá trị hiện tại từ cơ sở dữ liệu sau khi đã được lưu và bất kỳ giá trị tự động gán nào (như ID) cũng được cập nhật.