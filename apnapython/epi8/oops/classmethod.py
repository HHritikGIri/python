#used to change anything in class
#static method doesn't do this thing

class person():
    name= "anonymous"

    @classmethod
    def changename(cls,name):
        cls.name = name

p1 = person()
p1.changename("rahul")
print(p1.name)
print(person.name)