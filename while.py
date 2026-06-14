#while loop to deposit money and withdraw money untill the balance is greater than 0
amount = int(input("Enter the amount: "))
while amount > 0:
    print("Deposit money ")
    if balance >= amount:
        balance -= amount
        print(f"Withdrawal successful. Remaining balance: {balance}")
    amount = int(input("Enter the amount: "))