#Methods are functions that belong to the objects.

# class student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks

#         def welcome(self):
#             print("Welcome student, ",self.name)

# s1= student("Hritik",97)
# s1.welcome()


#static methods: Methods that don't use the self parameter , work at class level
# class Student:
#     @staticmethod #decorator
#     def college():
#         print("ABC college")


#question

class account:
    def __init__ (self,balance,acc_no):
        self.balance = balance
        self.acc_no = acc_no

        #debit method
        def debit(self,amount):
            self.balance -= amount
            print("rs", amount, "was debited")
            print("bal=",self.get_balance())

        #credit method
        def credit(self,amount):
            self.balance += amount
            print("rs", amount ,"was credited")
            print("bal=",self.get_balance())

        def get_balance(self):
            return self.balance 

acc1 = account(10000,12347)

acc1.debit(500)
acc1.credit(1000)


