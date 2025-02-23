import math

def mod_exp(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

# Bước 1: Khởi tạo các giá trị
p = 17
q = 23
n = p * q
phi_n = (p - 1) * (q - 1)
e = 5

# Bước 2: Chuyển thông điệp thành số
def text_to_numbers(text):
    return [ord(char) for char in text]

P = "BuiThiThuong"
numeric_message = text_to_numbers(P)

# Bước 3: Mã hóa từng ký tự
encrypted_message = [mod_exp(m, e, n) for m in numeric_message]

print("Thông điệp gốc:", P)
print("Dạng số:", numeric_message)
print("Dạng mã hóa:", encrypted_message)