print(r"Line A \n Line B")  # after writing r, before double quote, escape sequences treated as normal string

# this is double \\ backslash
print(r"this is double \\ backslash")

# these are /\/\/\/\/\ mountains
print(r"these are /\/\/\/\/\\") # we can't use raw string here

# he is     awesome
print(r"he is \t awesome")

# \" \n \t \'
print(r"\" \n \t \'")


# print Emoji
print("\U0001F612")