# THAM SỐ ĐƯỜNG DẪN ĐƯỢC XÁC ĐỊNH TRƯỚC
from enum import Enum
from fastapi import FastAPI

app = FastAPI()


@app.get("/item/{item_id}")
def root(item_id: int):        # int giúp kiểm tra kiểu dữ liệu đầu vào, nếu không đúng sẽ không hoạt động
    return f'item : {item_id}'

# Hoặc có thể định nghĩa tham số đường dẫn đầu vào thông qua Enum
# ModelName là một Enum định nghĩa ba mô hình: alexnet, resnet, và lenet.
# Endpoint /models/{model_name} sẽ chỉ chấp nhận các giá trị model_name là một trong ba giá trị trên.
# Nếu người dùng gửi một giá trị không hợp lệ, FastAPI sẽ trả về lỗi 422.


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}
