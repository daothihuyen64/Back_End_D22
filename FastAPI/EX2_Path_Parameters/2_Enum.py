#Enum dùng để tạo các hằng số có tên gọi và giá trị cụ thể - không bao giờ thay đổi
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

# Sử dụng Enum
print(Color.RED)          # Output: Color.RED
print(Color.RED.name)     # Output: RED
print(Color.RED.value)    # Output: 1