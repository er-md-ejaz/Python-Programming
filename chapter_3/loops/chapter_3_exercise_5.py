name = input("Enter your name: ")
length = len(name)
i = 0
temp = ""
while i < length:
    if name[i] not in temp:
        print(f"{name[i]}:{name.count(name[i])}")
        temp += name[i]
    i += 1