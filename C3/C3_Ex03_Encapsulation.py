#%% Định nghĩa lớp Bank Account
class BankAccount:
    def __init__(self, owner,balance):
        self.owner = owner
        self.__balance = balance #Biến private (chỉ truy cập nội bộ)

    def deposit(self,amount):
        """Gửi tiền vào TK"""
        if amount > 0:
            self.__balance += amount
            print(f"Deposit {amount}, New Balance: {self.__balance}")

    def withdraw(self,amount):
        """Rút tiền từ TK"""
        if 0 < amount < self.__balance:
            self.__balance -= amount
            print(f"Withdraw {amount}, New Balance: {self.__balance}")
        else:
            print("Insufficient balance!")

    def get_balance(self):
        """Lấy số dư (Encapsulation)"""
        return self.__balance

#%% Tạo Bank Account
account = BankAccount("Japan",1000)

#%% Gửi và rút tiền

account.deposit(100)
account.withdraw(500)

#%% Truy cập số dư an toàn
print("Current Balance:", account.get_balance())

#%% Cố tình truy cập biến private (sẽ gây lỗi)
print(account.get_balance()) #Lỗi vì __balance là private