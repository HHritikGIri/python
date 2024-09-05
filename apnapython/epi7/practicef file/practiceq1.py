with open("C:\\Users\\hriti\\OneDrive\\Desktop\\apnapython\\epi7\\practicef file\\practice.txt","r") as f:
#     f.write("Hi everyone\nwe are learning File I/O\n")
#     f.write("using Java.\nI like programming in Java.")

    data = f.read()

new_data=data.replace("Java","Python")
print(new_data)

with open("C:\\Users\\hriti\\OneDrive\\Desktop\\apnapython\\epi7\\practicef file\\practice.txt","w") as f:
    f.write(new_data)


with open("C:\\Users\\hriti\\OneDrive\\Desktop\\apnapython\\epi7\\practicef file\\practice.txt","r") as f:
    data=f.read()
    if(data.find("learning") != -1):
        print("found")
        


