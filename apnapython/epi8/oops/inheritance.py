#single level

# class car:
#     color = "black"
#     @staticmethod
#     def start():
#         print("car started..")


#     @staticmethod
#     def stop():
#         print("car stopped..")

# class toyotacar(car):
#     def __init__(self,name):
#         self.name=name

# car1=toyotacar("fortuner")
# car2=toyotacar("innova")

# print(car1.start())


#multilevel

# class car:
#     @staticmethod
#     def start():
#         print("car started..")

#     @staticmethod
#     def stop():
#         print("car stopped..")

# class toyotacar(car):
#     def __init__(self,brand):
#         self.brand = brand

# class fortuner(toyotacar):
#     def __init__(self,name):
#         self.name = name

# car1=fortuner("diesel")
# car1.start()


#multiple inheritance

class A:
    varA="welcome to A"

class B:
    varB="welcome to B"

class C(A,B):
    varC="welcome to C"

c1=C()

print(c1.varC)
print(c1.varB)
print(c1.varA)
