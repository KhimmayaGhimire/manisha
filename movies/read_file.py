# print(f"cursior pointer{f.tell()}")
# print(f.read())
# print(f"cursior pointer{f.tell()}")
# print("before seek")
# print(f.seek(0))

# print(f.read())
# print("after seek")
# print(f"cursior pointer{f.tell()}")

f=open("hub.txt")
# print(f.readline(),end="")
# print(f.readline(),end="")
# lines=f.readlines()
# print(lines)

# for line  in lines:
#     print(line,end="")
#     print(len(line))

# f.close()

with open("hub.txt","r")as f:
    data_reader=f.read()
    print(data_reader)

