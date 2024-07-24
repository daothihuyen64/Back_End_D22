from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

# Tạo engine để kết nối tới cơ sở dữ liệu
engine = create_engine(DATABASE_URL)
# Tạo session để giao tiếp với cơ sở dữ liệu
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Tạo base class cho các mô hình
Base = declarative_base()


class User(Base):
    __tablename__ = "fastapi_test2"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), index=True)


# Tạo tất cả các bảng trong cơ sở dữ liệu
Base.metadata.create_all(bind=engine)
