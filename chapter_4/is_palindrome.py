# def is_palindrome(name):
#     name2 = name[-1: :-1]
#     if name==name2:
#         return "palindrome"
#     return "not palindrome"

# def is_palindrome(name):
#     if name == name[: : -1]:
#         return "palindrome"
#     return "not palindrome"

def is_palindrome(name):
    return name == name[: : -1]

print(is_palindrome("madan"))
print(is_palindrome("madam"))