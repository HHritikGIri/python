class student:
    def __init__(self,phy,chem,maths):
        self.phy=phy
        self.chem=chem
        self.maths=maths


    @property
    def percentage(self):
        return str((self.phy + self.chem +self.maths) / 3) + "%"
    

stu1 = student(98,97,99)
print(stu1.percentage)

stu1.phy=82
print(stu1.percentage)
