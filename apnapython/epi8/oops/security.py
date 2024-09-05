class account:
    def __init__(self,acc_no,__acc_pass):
        self.acc_no = acc_no
        self.acc_pass = __acc_pass

    def resetpass(self):
        print(self.__acc_pass) #ye chal jayega kyuki class ke andar hai

acc1 = account(12345,"abcde")

print(acc1.__acc_no)
print(acc1.acc_pass) #nhi chalega kyuki class ke bahar hai



#another example

class person():
    __name = "anonymous"

    def __hello(self):
        print("hello person!")

    def welcome(self):
        self.__hello()  #welcome hello ko call kar rha hai

p1=person()
print(p1.welcome)  #p1 welcome ko call kar rha hai

