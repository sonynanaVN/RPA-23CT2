import sys
sys.stdout.reconfigure(encoding='utf-8')

from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary

    def display_info(self):
        print(f"ID: {self.id}, Name: {self.name}, Salary: {self.get_salary()}")

    @abstractmethod
    def calculate_salary(self):
        pass


class Developer(Employee):
    def __init__(self, id, name, salary, programming_language, overtime_hours):
        super().__init__(id, name, salary)
        self.programming_language = programming_language
        self.overtime_hours = overtime_hours

    def calculate_salary(self):
        return self.get_salary() + self.overtime_hours * 200

    def display_info(self):
        super().display_info()
        print(f"Language: {self.programming_language}, Overtime: {self.overtime_hours}")


class Manager(Employee):
    def __init__(self, id, name, salary, bonus):
        super().__init__(id, name, salary)
        self.bonus = bonus

    def calculate_salary(self):
        return self.get_salary() + self.bonus

    def display_info(self):
        super().display_info()
        print(f"Bonus: {self.bonus}")


dev = Developer(1, "An", 1000, "Python", 10)
mgr = Manager(2, "Binh", 2000, 500)

print("=== Developer ===")
dev.display_info()
print("Lương thực nhận:", dev.calculate_salary())

print("\n=== Manager ===")
mgr.display_info()
print("Lương thực nhận:", mgr.calculate_salary())