def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def in_so_nguyen_to(n):
    print(f"Các số nguyên tố từ 2 đến {n} là:")
    for num in range(2, n + 1):
        if la_so_nguyen_to(num):
            print(num, end=" ")

# Nhập số từ người dùng
n = int(input("Nhập một số nguyên dương: "))

# In các số nguyên tố
in_so_nguyen_to(n)