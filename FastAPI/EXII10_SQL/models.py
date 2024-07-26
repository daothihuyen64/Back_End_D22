from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(50), unique=True, index=True)
    hashed_password = Column(String(50))
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "iteme"

    id = Column(Integer, primary_key=True)
    title = Column(String(50), index=True)
    description = Column(String(50), index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")

# relationship để tạo quan hệ giữa các bảng:
# khi truy cập my_user.items sẽ trả về các items mà my_user đã mua
# khi truy cập item_a.owner sẽ trả về users đã mua item_a
