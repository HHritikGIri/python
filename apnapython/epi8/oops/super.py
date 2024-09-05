# super() is a method which is used to access methods of the parent class

class car:
    def __init__(self,type):
        self.type = type

    @staticmethod
    def start():
        print("Car started..")

    @staticmethod
    def stop():
        print("car stopped..")

class toyotacar(car):
    def __init__(self,name,type):
        super().__init__(type)
        self.name=name
        super().start()

car1=toyotacar("prius","electric")
print(car1.type)