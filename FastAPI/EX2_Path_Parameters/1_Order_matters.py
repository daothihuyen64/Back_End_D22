from fastapi import FastAPI

app = FastAPI()


@app.get('/infor/me')
def read_infor_individual():
    return 'user_name : me'


@app.get('/infor/{user_id}')
def read_infor_id(user_id: str):
    return f'user_id: {user_id}'

# ?1 : Đặt @app.get('/infor/{user_id}') lên trước @app.get('/infor/me') có được không?
# trl: không được. Vì khi đó nếu nhập đường dẫn /users/me thì đường dẫn cho /users/{user_id} cũng sẽ khớp với /users/me, "nghĩ rằng" nó đang nhận một tham số user_id có giá trị là "me".
# kết luận : thứ tự cũng quan trọng
