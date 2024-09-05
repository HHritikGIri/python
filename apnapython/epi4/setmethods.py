setji={10,23,19,33,88,12}
setji2={77,88,22,12}

setji.add(43)
print(setji)

setji.remove(10)
print(setji)

setji.pop() #Removes a random value
print(setji)

set=setji.union(setji2)
print(set)

set2=setji.intersection(setji2)
print(set2)

setji.clear()
print(setji)