class customer:

    def __init__(self) :

        self.balance=0

    def deposit(self, money):

        self.balance+=money
        
        print(f"You have just added {money} to you balance!,this your updated balance ('u')/:",self.balance)

    def withdrawal(self,amount):

        if self.balance>=amount:
            
            self.balance-=amount
            print (f"You withdraw => {amount},this is your updated balance (^u^)/" ,self.balance)
            
        else:
            print("Insufficient balance!, try again later('-')")

    def myBalance(self):

        print("This is your balance (OuO)/:",self.balance)
         
