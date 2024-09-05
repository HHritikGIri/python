info = {
    "name": "Hritik" ,
    "subjects": ["English", "Hindi", "SE"],
    "topics" : ("dict","sets"),
    "age": 35,
    "is_adult": True,
    "marks" : 94
}
print(info)

#dict are mutable
info["name"] = "shraddha"
print(info["name"])


#nested dictionary:

student= {
    "Name": "hritik",
    "roll_no": 24,
    "Score": {
        "phy":88,
        "chem":97,
        "maths":99

    }
}

print(student["Score"]["maths"])