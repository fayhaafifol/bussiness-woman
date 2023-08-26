from bank import lebank
from customer import customer

mybank = lebank()

while True:

    print("Choose what you want to do (^w^):")
    print("===================================")
    print("1) Create account")
    print("2) Deposit Money")
    print("3) Withdraw Money")
    print("4) transfer Money")
    print("5) See My Balance")

    choice=int(input(">"))

    match choice:

        case 1:

            username = input("Please enter a username (>w<):")

            mybank.create_acc(username)

            

            #if lebank.get_user(username) == user:

                #print("error: username already exist")

                #continue

        case 2:

            username = input("Please enter your username ('w'):")
            
            mycustomer = mybank.get_user(username)

            if mycustomer == 0:

                continue

            money=int(input("Enter the amount of money you want to deposit ('o'):"))

            mycustomer.deposit(money)


        case 3:

            username = input("Please enter your username ('w'):")

            mycustomer = mybank.get_user(username)

            if mycustomer == 0:

                continue

            amount=int(input ("Enter the amount of money to be Withdraw (^w^):"))

            mycustomer.withdrawal(amount)

        case 4:

            send_username = input("Enter the username of the sender ('u'):")
            
            mycustomer = mybank.get_user(send_username)

            if mycustomer == 0:

                continue

            rec_username = input("Enter the username of the reciever (UwU):")

            mycustomer1 = mybank.get_user(rec_username)

            if mycustomer1 == 0:

                continue

            trans_money= int(input("How much do you want to transfer? (-u-):"))

            mybank.transfer(mycustomer, mycustomer1,trans_money)

        case 5:

            username = input("Please enter your username ('w'):")

            mycustomer = mybank.get_user(username)

            if mycustomer == 0:

                continue
            
            mycustomer.myBalance()

        case _:

            print("error: inavlid input")






