from pydantic import BaseModel

# mô hình nhận dữ liệu vào csdl
class ItemBase(BaseModel):
    title: str
    description: str | None = None


class ItemCreate(ItemBase):
    pass

# mô hình trả dữ liệu
class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True

# mô hình nhận dữ liệu vào csdl
class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str

# mô hình trả dữ liệu 
class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        from_attributes = True

# Pydantic mặc định yêu cầu dữ liệu đầu vào phải là các dict hoặc các kiểu dữ liệu tiêu chuẩn khác.

# orm_mode = True :

#   1. Pydantic có thể nhận các đối tượng ORM, ánh xạ các bảng trong cơ sở dữ liệu thành các lớp trong mã nguồn.

#   2. Khi trả về dữ liệu sẽ bao gồm cả dữ liệu có quan hệ . 
#      vd: lấy thông tin user thì trả về cả thông tin item tương ứng,
#      nếu không bật orm_mode thì sẽ không trả về dữ liệu có quan hệ.
