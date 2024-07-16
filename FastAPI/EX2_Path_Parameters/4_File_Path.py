# THAM SÔ ĐƯỜNG DẪN CHỨA ĐƯỜNG DẪN

from fastapi import FastAPI

app = FastAPI()

# file_path : path -> file_path được chứa ký tự '/
# so sánh giữa có sử dụng ': path' và không sử dụng ': path'

# 1. SỬ DỤNG ': path'


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}

# URL /files/some/file/path/here sẽ nhận giá trị some/file/path/here cho file_path.


# 2. KHÔNG SỬ DỤNG ': path'

@app.get("/files/{file_path}")
async def read_file(file_path: str):
    return {"file_path": file_path}

# URL /files/some/file/path/here sẽ bị lỗi.
# URL /files/some sẽ nhận giá trị some cho file_path.
