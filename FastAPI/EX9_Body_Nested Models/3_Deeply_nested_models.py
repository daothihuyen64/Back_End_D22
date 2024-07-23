from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()


class Image(BaseModel):                 # Mô hình 1
    url: HttpUrl
    name: str


class Item(BaseModel):                  
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()
    images: list[Image] | None = None   # Mô hình 2 chứa danh sách mô hình 1

class Offer(BaseModel):                   
    name: str
    description: str | None = None
    price: float
    items: list[Item]                   # Mô hình 3 chứa danh sách mô hình 2


@app.post("/offers/")
async def create_offer(offer: Offer):
    return offer