age = input("Enter your age: ")
age = int(age)

# if age >= 14:
#     print("you can play game")
# else:
#     print("you can't play")


# pass statement
# if age >= 14:
#     pass

# if elif else statement
if 0 < age <= 3:
    print("ticket price is free")
elif 3 < age <= 10:
    print("ticket price is 150")
elif 10 < age <= 60:
    print("ticket price is 250")
else:
    print("ticket price is 200")
