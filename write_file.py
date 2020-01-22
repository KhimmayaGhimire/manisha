# with open("file.txt","w")as f:
#     data=f.write("i am from butwal")
#     print(data)

# with open("file.txt","a")as f:
#     data=f.write("i am from bhairawa")
#     print(data)

# with open("file.txt","a")as f:
#     f.write("i am from bhairawa")

# with open("file.txt","r+")as f:
#     f.seek(len(f.read()))
#     f.write("this is hub it")

with open("hub.txt","r")as rf:
    with open("file1.txt","w")as wf:
        wf.write(rf.read())



