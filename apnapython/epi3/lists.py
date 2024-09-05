#Stores elements of different datatypes together(integer,float,string,etc.)

#Lists are Mutable while Strings are immutable

student=["Hritik",98,88.5]
print(student)


Marks=[90,91,92,95]
print(Marks)
print(len(Marks)) #length of list
print(Marks[1]) #prints 91

Marks[0]=31 #value will change to 31 replacing 90

print(Marks)


#List Slicing

print(Marks[0:2])  #prints 0th,1th indices

#based on negative indices
print(Marks[-3:-1])  #prints 91,91

pallindrome=[1,3,4,2,1]
copy=pallindrome.copy()
copy.reverse()

if(pallindrome==copy):
    print("The list is pallindrome")

else:
    print("The list is not a Pallindrome")





