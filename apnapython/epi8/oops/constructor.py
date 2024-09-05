#constructor

#All classes have a function called _init_(),which is always executed when the object is being initiated

class student:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        print("adding new student to Database...")

s1 = student("Hritik",96)
print(s1.name,s1.marks)  # Hritik


