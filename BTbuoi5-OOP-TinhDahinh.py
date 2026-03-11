import sys
sys.stdout.reconfigure(encoding='utf-8')
class DongVat:
    def keu(self):
        print("Động vật kêu")


class Cho(DongVat):
    def keu(self):
        print("Chó sủa")


class Meo(DongVat):
    def keu(self):
        print("Mèo kêu meo meo")


a = Cho()
b = Meo()

a.keu()   # Chó sủa
b.keu()   # Mèo kêu meo meo
# Tính đa hình trong OOP cho phép các đối tượng thuộc các lớp khác nhau có thể được xử lý thông qua cùng một giao diện. Trong ví dụ trên, cả lớp Cho và Meo đều kế thừa từ lớp DongVat và đều có phương thức keu(). Khi chúng ta gọi phương thức keu() trên các đối tượng a và b, Python sẽ tự động xác định lớp của đối tượng và gọi phương thức keu() tương ứng, cho phép chúng ta xử lý các đối tượng khác nhau một cách linh hoạt mà không cần phải biết chính xác loại của chúng.
#Bài tập: Tính đa hình trong OOP với lớp Employee, Developer và Manager
class Employee:
    def __init__(self, salary):
        self.salary = salary

    def calculate_salary(self):
        return self.salary


class Developer(Employee):
    def calculate_salary(self):
        return self.salary + self.salary * 0.2   # thưởng 20%


class Manager(Employee):
    def calculate_salary(self):
        return self.salary + self.salary * 0.3   # thưởng 30%


# Test
e = Employee(1000)
d = Developer(1000)
m = Manager(1000)

print("Employee salary:", e.calculate_salary())
print("Developer salary:", d.calculate_salary())
print("Manager salary:", m.calculate_salary())