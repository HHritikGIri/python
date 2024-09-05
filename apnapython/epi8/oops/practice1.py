class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum = sum+val
        print("Hii",self.name,"your avg score is:",sum/3)

s1 = student("Hritik",[99,98,97])
s1.get_avg()
