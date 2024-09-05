#used for sequential traversal

#for __ in __:
    #some work

# veggies=["potato","brinjal","Ladyfinger"]

# for el in veggies:
#     print(el)

list=[1,4,9,16,25,36,49,64,81,100]

# for el in list:
#     print(el)

x=49
idx=0
for el in list:
    if(el==x):
        print("Found at index=",idx)
        idx+=1
    else:
        print("finding")