name = input("Enter your name: ")
age = int(input("Enter your age: "))

if (name[0] == 'a' or name[0] == 'A') and age >= 10:
    print("you can watch coco")
    # print(name[2])
else:
    print("sorry, you can't watch coco")