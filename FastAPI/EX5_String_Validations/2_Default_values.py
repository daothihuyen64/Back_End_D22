from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: Annotated[str, Query(default="fixedquery", min_length=3)]):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# giá trị mặc định của q là fixedquery
# cách khác để khai báo giá trị mặc định : async def read_items(q: Annotated[str, Query(min_length=3)] = "fixedquery"):
