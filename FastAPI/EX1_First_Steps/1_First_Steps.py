from fastapi import FastAPI

app = FastAPI()  # tạo 1 instance (object) từ class FastAPI

# định nghĩa route (đường dẫn)
# hàm read_root sẽ được sử dụng để xử lý các yêu cầu get (lấy dữ liệu) từ http://127.0.0.1:8000/XIN_CHAO
# nó sẽ thực hiện các logic trong hàm read_root đã định nghĩa và trả kết quả 'Hello' dưới dạng JSON (dữ liệu nhẹ - dùng để giao tiếp giữa client và sever)


@app.get("/XIN_CHAO")
async def read_root():
    return 'Hello'
