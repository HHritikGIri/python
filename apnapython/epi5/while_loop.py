#While Loops
   #syntax
    # while condition :
    #some work

num=100
while num >=1:
    print("Hello python",num)
    num=num-1

# number = int(input("Enter a Number"))
# i=1
# while (i<=10):
#     print(number*i,i)
#     i=i+1

#question

# nums = [1,4,9,16,25,36,49,64,81,100]
# idx=0
# while idx < len(nums):
#     print(nums[idx])
#     idx+=1

#question

tup=(1,4,9,16,25,36,49,64,81,100)
x=36
idx=0
while idx < len(tup):
    if(tup[idx]==x):
        print("Found",idx)
    idx+=1


