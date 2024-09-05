# def sum(a,b):
#     sum = a+b
#     return sum

# sum(10,4)

# def avg(a,b,c):
#     summ= a+b+c
#     average=summ / 3
#     print(average)

# avg(21,2,0)

list=[2,5,2,5,7,0,9]
def listwa(list):
    print(len(list))
    return len(list)

# listwa(list)

def items(list):
    for item in list:
        print(item,end=" ")

# items(list)

def fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)

# fact(5)

# USD to INR

def doll(n):
    dollar=83
    for i in range(1,n+1):
        INR=dollar*i
    print(INR)

doll(2)