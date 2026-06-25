class MobileMoney:
    def __init__(self, balance):
        self.__balance = balance # private attribute

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient balance!")

    def check_balance(self):
        return self.__balance


# Testing the application
input_balance = int(input("Enter initial balance: "))
account = MobileMoney(input_balance)
input_deposit = int(input("Enter amount to deposit: "))
account.deposit(input_deposit)
input_withdrawal = int(input("Enter amount to withdraw: "))
account.withdraw(input_withdrawal)

print("Current Balance:", account.check_balance())