name, char = input("Enter your name and character: ").split(",")
# print(f"Length of name is: {len(name)}, and no. of {char} is {name.lower().count(char.lower())}")


print(f"Length of name is: {len(name)} and no. of {char} is {name.lower().strip().count(char.lower().strip())}")