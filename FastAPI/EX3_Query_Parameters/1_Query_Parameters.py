# 1.Query Parameters (tham số truy vấn) là các tham số được gửi kèm theo URL sau dấu ?
# 2.các tham số được khai báo trong hàm mà không phải tham số đường dẫn thì được gọi là tham số truy vấn.
#   q là tham số truy vấn
#   item_id là tham số đường dẫn
# 3.tham số truy vấn được sử dụng để lọc hoặc tùy chỉnh dữ liệu trả về từ API.
# 4.tham số truy vấn là 1 phần không bắt buộc trong đường dẫn.
#   http://127.0.0.1:8000/items/hh
#   http://127.0.0.1:8000/items/hh?q=c

from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}
