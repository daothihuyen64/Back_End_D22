from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax  # có thể truy cập trực tiếp vào tất cả các thuộc tính của đối tượng mô hình
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict