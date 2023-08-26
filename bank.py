from customer import customer

class lebank:


    def __init__(self):


        self.database ={} #{username:user}

    def create_acc(self,username):

        user = customer()

        self.database[username] = user

    def get_user(self,username):

        if username in self.database:

            user = self.database[username]
       
            return user
        
        else:

            print("error: username not found")

            return 0
        

    def transfer(self,send_username,rec_username,trans_money):

        send_username.withdrawal(trans_money)

        rec_username.deposit(trans_money)




