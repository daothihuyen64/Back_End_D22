from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(
    q: Annotated[
        str | None,
        Query(
            #  đây là trường hợp tổng quát bao gồm nhiều quy tắc của biến, các quy tắc này là tùy chọn, có thể định nghĩa hoặc không tùy mục đích.
            alias="item-query",  # trong URL sẽ sử dụng item-query thay cho d
            title="Query string",  # trong docs tilte của q là "Query string"
            description="Query string for the items to search in the database that have a good match",
            min_length=3,  # item-query có độ dài min là 3
            max_length=50,  # item-query có độ dài max là 50
            pattern="^fixedquery$",  # định nghĩa cú pháp cho item-query: ^ bắt đầu là fixedquery, $ là kết thúc -> item-query chỉ được là: fixedquery
            deprecated=True,  # thông báo biến này hiện không còn sử dụng nữa
        ),
    ] = None, # = None :giá trị mặc định của q là None, gía trị này có thể thay đổi tùy người code định nghĩa.
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
