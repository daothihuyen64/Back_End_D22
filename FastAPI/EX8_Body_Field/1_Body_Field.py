from typing import Annotated

from fastapi import Body, FastAPI
from pydantic import BaseModel, Field # khai báo thư viện

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = Field(
        default=None, title="The description of the item", max_length=300
    ) # thêm ràng buộc cho description 
    price: float = Field(gt=0, description="The price must be greater than zero") # thêm ràng buộc cho price
    tax: float | None = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
    results = {"item_id": item_id, "item": item}
    return results

# trong hàm muốn ràng buộc dữ liệu thì dùng Annotated
# trong mô hình muốn ràng buộc dữ liệu dùng Field

