from fastapi import FastAPI

app = FastAPI()


@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(user_id: int, item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

# 1. giá trị mặc định short : mặc định là false
# 2. giá trị tùy chọn q : mặc định là None (str | None : có nghĩa là dữ liệu của q có thể là string hoặc None , không khai báo thì mặc định là None (= None))
# 3. có thể thử truy cập vào các đường dẫn sau đây
#   http://127.0.0.1:8000/users/1/items/id_01?short=0
#   http://127.0.0.1:8000/users/2/items/id_02?short=True
#   http://127.0.0.1:8000/users/3/items/id_03?short=true
#   http://127.0.0.1:8000/users/4/items/id_04?short=on
#   http://127.0.0.1:8000/users/4/items/id_04?short=yes

fake_items_db = [{"item_name": "Foo"}, {
    "item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]

# 3. skip = 0 và limit = 10 cũng là 2 giá trị mặc định
# 4. có thể thử truy cập vào các đường dẫn sau đây
#   http://127.0.0.1:8000/items/
#   http://127.0.0.1:8000/items/?skip=0&limit=10
#   http://127.0.0.1:8000/items/?skip=20 (tại đường dẫn này skip = 20 và limit= 10)
