#  Example-2

# num = input("Enter a number: ")
# sum = 0
# for i in range(len(num)):
#     sum += int(num[i])
# print(sum)

#  Example-3

name = input("Enter your name: ")
temp = ""
for i in range(len(name)):
    if name[i] not in temp:
        temp += name[i]
        print(f"{name[i]}:{name.count(name[i])}")
