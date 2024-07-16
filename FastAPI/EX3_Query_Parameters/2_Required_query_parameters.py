# Required query parameters (tham số truy vấn bắt buộc) trong FastAPI là các tham số truy vấn mà người dùng phải cung cấp khi gửi yêu cầu tới endpoint.
# Nếu các tham số này không được cung cấp, API sẽ trả về lỗi.
# Để định nghĩa một query parameter là bắt buộc, chỉ cần không cung cấp giá trị mặc định cho tham số đó trong hàm định nghĩa endpoint.

from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item

# needy là tham số truy vấn bắt buộc có kiểu str.
# vì needy là bắt buộc nên nếu truy cập vào đường dẫn ko truyền tham số needy sẽ bị lỗi:
#   đường dẫn lỗi:       http://127.0.0.1:8000/items/foo-item
#   đường dẫn chính xác: http://127.0.0.1:8000/items/foo-item?needy=sooooneedy
