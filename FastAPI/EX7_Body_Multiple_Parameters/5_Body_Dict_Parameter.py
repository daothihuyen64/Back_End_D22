from fastapi import FastAPI

app = FastAPI()


@app.post("/index-weights/")
async def create_index_weights(weights: dict[int, float]):
    return weights

# weight là dict với các cặp key:value thỏa mãn:
# key : kiểu int
# value: kiểu float
