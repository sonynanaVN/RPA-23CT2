from abc import ABC, abstractmethod


# ========================
# 1️⃣ TRỪU TƯỢNG (Abstraction)
# ========================
class Person(ABC):
    def __init__(self, name):
        self.name = name  # public

    @abstractmethod
    def work(self):
        pass


# ========================
# 2️⃣ KẾ THỪA (Inheritance)
# ========================
class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.__salary = salary  # private

    def get_salary(self):  # public method
        return self.__salary


class Developer(Employee):
    def work(self):  # ĐA HÌNH
        print(f"{self.name} is coding...")


class Manager(Employee):
    def work(self):  # ĐA HÌNH
        print(f"{self.name} is managing the project...")


# ========================
# 3️⃣ CLASS TASK
# ========================
class Task:
    def __init__(self, title):
        self.title = title
        self.status = "Todo"

    def complete_task(self):
        self.status = "Done"


# ========================
# 4️⃣ CLASS PROJECT
# ========================
class Project:
    def __init__(self, name, budget):
        self.name = name
        self.__budget = budget  # private
        self.members = []
        self.tasks = []

    def add_member(self, employee):
        self.members.append(employee)

    def add_task(self, task):
        self.tasks.append(task)

    def show_info(self):
        print(f"\nProject: {self.name}")
        print(f"Budget: {self.__budget}")
        print("Members:")
        for m in self.members:
            print("-", m.name)
        print("Tasks:")
        for t in self.tasks:
            print("-", t.title, "|", t.status)


# ========================
# 5️⃣ TEST CHƯƠNG TRÌNH
# ========================
dev1 = Developer("An", 1500)
manager1 = Manager("Binh", 3000)

project = Project("AI System", 50000)

project.add_member(dev1)
project.add_member(manager1)

task1 = Task("Build API")
task2 = Task("Train AI Model")

project.add_task(task1)
project.add_task(task2)

dev1.work()
manager1.work()

task1.complete_task()

project.show_info()