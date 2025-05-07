# input function always store values in the form of string

# name = input("What's your name? ")
# age = input("What's your age? ")

# print("Hello " + name)
# print("Your age is " + age)

#! Taking two input in one line
name, age = input("Enter your name and age: ").split() #it is separated by white_space
print(name)
print(age)

name, age = input("Enter your name and age: ").split(",") #it is separated by comma
print(name)
print(age)
