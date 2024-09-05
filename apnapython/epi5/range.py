#Range function returns a seqeunce of numbers,starting from 0 by default,and increments by 1(by default),and stops before a specified number

#range(start?,stop,step?)
# for i in range(6):
#     print(i)

# for i in range(1,5):
#     print(i)

# for i in range(2,10,2):
#     print(i)

#quest

#1-100

# for i in range(1,101):
#     print(i)

# for i in range(100,0,-1):
#     print(i)

# x=int(input("enter a number"))

# for i in range(1,11):
#     print(x*i)

n=5
fact=1

for i in range(1,n+1):
    fact*=i

print(fact)
