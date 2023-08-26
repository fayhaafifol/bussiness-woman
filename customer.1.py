class customer:
    def __init__(self) :
        self.balance=0

    def deposit(self):
        money=int(input("enter the number you want to deposit:"))
        self.balance+=money
        print("you have just added ",self.balance)
user=customer()

user.deposit()