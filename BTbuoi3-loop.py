#PT bậc 2
import math

a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))

if a == 0:
    if b == 0:
        print("Phương trình vô nghiệm" if c != 0 else "Phương trình vô số nghiệm")
    else:
        x = -c / b
        print("Nghiệm:", x)
else:
    delta = b*b - 4*a*c
    if delta < 0:
        print("Phương trình vô nghiệm")
    elif delta == 0:
        x = -b / (2*a)
        print("Nghiệm kép:", x)
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print("Hai nghiệm:", x1, x2)
