student= {
    "Name" : "hritik",
    "Roll_no" : 26,
    "score" : {
        "maths": 99,
        "phy" : 78,
        "chem" : 76
    }
}


print(student.keys())
print(student.values())
print(student.items())  #returns all key value pairs as tuples
print(student.get("Name")) #returns the key according to value

student.update({"city" : "delhi"})
print(student) #inserts the specified items to the dictionary