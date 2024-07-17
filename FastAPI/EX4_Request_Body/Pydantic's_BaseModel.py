from fastapi import FastAPI
from pydantic import BaseModel

# b1 : Định nghĩa mô hình dữ liệu


class Item(BaseModel):
    name: str
    description: str | None = None # trong dữ liệu json gửi đến sever có thể ko cần vì ở dạng tùy chọn
    price: float
    tax: float | None = None  # dạng tùy chọn


app = FastAPI()

# b2: Định Nghĩa Endpoint POST


@app.post("/items/")
async def create_item(item: Item):
    return item

# khi chạy fastapi sẽ:
# 1. Đọc nội dung gửi đến dưới dạng JSON.
# 2. Chuyển đổi các loại tương ứng (nếu cần - hỗ trợ chuyển đổi các kiểu dữ liệu để phù hợp với kiểu đã định nghĩa).
# 3. Xác thực dữ liệu. Nếu dữ liệu không hợp lệ, nó sẽ trả về một lỗi rõ ràng và chính xác, chỉ ra chính xác dữ liệu không chính xác ở đâu và dữ liệu nào.
# 4. Cung cấp dữ liệu nhận được trong tham số item.
# 5. Trả về JSON schema hiển thị trong API docs.
