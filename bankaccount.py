class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name

    def deposit(self, amount):
        self.balance += amount
        return amount

    def withdraw(self, amount):
        if self.balance < amount:
            return "Insufficient balance"
        else:
            self.balance -= amount
            return amount

    def check_balance(self):
        print("Current Balance:", self.balance)

    def customer_details(self):
        print("Customer Name:", self.customer_name)
        print("Account Number:", self.account_number)
        print("Date of Opening:", self.date_of_opening)
        print("Balance:", self.balance)


account1 = BankAccount("1234567891", 5000, "03-07-2026", "Levis Kibet")

account1.customer_details()

print("\nAmount Deposited:", account1.deposit(2000))

print("Amount Withdrawn:", account1.withdraw(1500))

print("Withdrawal Attempt:", account1.withdraw(10000))

account1.check_balance()
