# Bài 1: Viết chương trình giải phương trình bậc 2: ax^2 + bx + c = 0
import sys
sys.stdout.reconfigure(encoding='utf-8')
import math  

# Nhập hệ số
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))


if a == 0:
    if b == 0:
        print("Phương trình vô nghiệm")
    else:
        print("Nghiệm:", -c / b)
else:

    delta = b**2 - 4*a*c

    if delta < 0:
        print("Phương trình vô nghiệm")
    elif delta == 0:
        print("Nghiệm kép:", -b / (2*a))
    else:
  
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print("Hai nghiệm:", x1, x2)
# Bài 2: In bảng cửu chương từ 2 đến 9

for i in range(2, 10):  
    print(f"\nBảng cửu chương {i}:")
    for j in range(1, 11):  
        print(f"{i} x {j} = {i*j}")
# Bài 3: Tính tổng các số chẵn từ 1 đến 100

tong = 0  

for i in range(2, 101, 2):  # Duyệt số chẵn
    tong += i  

print("Tổng là:", tong)
# Bài 4: Kiểm tra số nguyên tố

n = int(input("Nhập số: "))


if n < 2:
    print("Không phải số nguyên tố")
else:
    la_snt = True  


    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            la_snt = False
            break

    if la_snt:
        print("Là số nguyên tố")
    else:
        print("Không phải số nguyên tố")
# Bài 5: In hình tam giác với chiều cao n

n = int(input("Nhập chiều cao: "))

for i in range(1, n + 1):
    print("*" * i)  # In i dấu *
# Bài 6: Tìm ƯCLN và BCNN của hai số

import math

a = int(input("Nhập a: "))
b = int(input("Nhập b: "))


ucln = math.gcd(a, b)


bcnn = abs(a * b) // ucln

print("ƯCLN:", ucln)
print("BCNN:", bcnn)
# Bài 7: Đếm số lượng chữ số của một số nguyên

n = int(input("Nhập số: "))


so_chu_so = len(str(abs(n)))  

print("Số chữ số:", so_chu_so)