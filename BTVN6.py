import sys
sys.stdout.reconfigure(encoding='utf-8')
from abc import ABC, abstractmethod

# ===== Lớp trừu tượng =====
class Account(ABC):
    def __init__(self, account_id, owner, balance=0):
        self.account_id = account_id
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Nạp {amount} thành công!")
        else:
            print("Số tiền không hợp lệ!")

    @abstractmethod
    def withdraw(self, amount):
        pass

    def display_info(self):
        print(f"ID: {self.account_id}")
        print(f"Chủ TK: {self.owner}")
        print(f"Số dư: {self._balance}")

# ===== Tài khoản tiết kiệm =====
class SavingsAccount(Account):
    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print(f"Rút {amount} thành công!")
        else:
            print("Không đủ tiền!")

# ===== Tài khoản thanh toán =====
class CheckingAccount(Account):
    def __init__(self, account_id, owner, balance=0, overdraft_limit=500):
        super().__init__(account_id, owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self._balance + self.overdraft_limit:
            self._balance -= amount
            print(f"Rút {amount} thành công!")
        else:
            print("Vượt quá hạn mức!")

# ===== Hệ thống quản lý =====
class BankSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, acc_type, account_id, owner):
        if acc_type == "saving":
            acc = SavingsAccount(account_id, owner)
        elif acc_type == "checking":
            acc = CheckingAccount(account_id, owner)
        else:
            print("Loại tài khoản không hợp lệ!")
            return
        
        self.accounts[account_id] = acc
        print("Tạo tài khoản thành công!")

    def get_account(self, account_id):
        return self.accounts.get(account_id, None)

# ===== Demo =====
bank = BankSystem()

# Tạo tài khoản
bank.create_account("saving", "001", "An")
bank.create_account("checking", "002", "Bình")

# Nạp tiền
acc1 = bank.get_account("001")
acc1.deposit(1000)

# Rút tiền
acc1.withdraw(200)

# Hiển thị
acc1.display_info()

print("------")

acc2 = bank.get_account("002")
acc2.deposit(500)
acc2.withdraw(800)  # dùng overdraft
acc2.display_info()