from sqlalchemy import create_engine
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
# Tạo base class cho các mô hình - các mô hình kế thừa Base sẽ được ánh xạ tới cơ sở dữ liệu
Base = declarative_base()


# trong phiên làm việc SessionLocal:
#   1. autocommit = False : không tự động ghi các thay đổi trong phiên làm việc vào cơ sở dữ liệu . Cần gọi commit() để ghi các thay đổi này.
#   2. autoflush = False : không tự động đẩy các thay đổi trong phiên làm việc và csdl trước mỗi truy vấn query.
#   3. blind = engine : liên kết phiên làm việc với csdl.