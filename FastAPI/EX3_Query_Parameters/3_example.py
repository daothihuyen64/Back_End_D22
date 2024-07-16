# Phân Trang với skip và limit

from fastapi import FastAPI
from typing import List

app = FastAPI()

fake_items_db = [{"item": f"item_{i}"} for i in range(100)]  # Tạo ra một danh sách giả lập với 100 mục

@app.get("/items/", response_model=List[dict])
async def read_items(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

# giả sử api trả về 1 danh sách chứa 100 mục fake_items_db = [{"item": f"item_{i}"} for i in range(100)]
# ta sẽ phân thành 10 trang mỗi trang chứa 10 mục
# khi truy cập : http://127.0.0.1:8000/items?skip=0&limit=10 hàm read_items sẽ trả về 10 mục đầu tiên từ 0 -> 9
# khi truy cập : http://127.0.0.1:8000/items?skip=10&limit=10 hàm read_items sẽ trả về 10 mục tiếp theo từ 10->19
