class student:
    college_name = "ABC"  #class attribute when some thing is common for every object we can add it to class attribute to save space in memory

    def __init__(self,name,marks):
        self.name = name #obj attribute
        self.marks = marks #obj att > class att
        print("adding new student to Database...")

s1 = student("Hritik",96)
print(s1.name,s1.marks)  # Hritik

print(student.college_name)
