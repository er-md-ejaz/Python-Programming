# maximum between two number
def maximum_num(a, b):
    if a>b:
        return a
    return b

# print(maximum_num(8, 6))


# maximum between three numbers
# def greater_num(a, b, c):
#     if a>b and a>c:
#         return a
#     elif b>a and b>c:
#         return b
#     return c
    
# print(greater_num(4, 5, -2))


# function inside function

def greatest(a, b, c):
    # bigger = maximum_num(a, b)
    # return maximum_num(bigger, c)
    return maximum_num(maximum_num(a, b), c)

print(greatest(456, 40, 239))