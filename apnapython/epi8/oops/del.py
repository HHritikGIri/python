#used to delete object properties or object itself

#syntax

class student :
    def __init__(self,name):
        self.name=name

s1 = student("Hritik")
print(s1)
del s1
print(s1)