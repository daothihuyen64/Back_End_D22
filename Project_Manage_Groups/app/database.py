from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

DATABASE_URL= "mysql+pymysql://root:root@localhost/group_management"
# Tạo engine để kết nối tới cơ sở dữ liệu
engine = create_engine(DATABASE_URL)
# Tạo session để giao tiếp với cơ sở dữ liệu
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Tạo base class cho các mô hình - các mô hình kế thừa Base sẽ được ánh xạ tới cơ sở dữ liệu
Base = declarative_base()
