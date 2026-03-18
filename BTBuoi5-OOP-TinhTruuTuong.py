from abc import ABC, abstractmethod
import sys
sys.stdout.reconfigure(encoding='utf-8')
class Payment(ABC):

    def __init__(self, account, balance, amount):
        self.account = account
        self.balance = balance
        self.amount = amount

    def check_account(self):
        return len(self.account) == 10 and self.account.isdigit()

    def check_balance(self):
        return self.balance >= self.amount

    @abstractmethod
    def calculate_fee(self):
        pass

    def pay(self):
        if not self.check_account():
            print("Số tài khoản không hợp lệ")
            return
        
        if not self.check_balance():
            print("Không đủ số dư")
            return

        fee = self.calculate_fee()
        total = self.amount + fee
        print(f"Thanh toán {self.amount}, phí {fee}, tổng trừ {total}")
#thanh toán 
class BankPayment(Payment):

    def calculate_fee(self):
        return self.amount * 0.02   # phí 2%
#thanh toán thẻ
class CreditCardPayment(Payment):

    def calculate_fee(self):
        return self.amount * 0.03   # phí 3%
    
# Test
p1 = BankPayment("1234567890", 1000000, 200000)
p2 = CreditCardPayment("9876543210", 500000, 200000)

p1.pay()
p2.pay()