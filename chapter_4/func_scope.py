#  basically we try to avoid this type of variables because it is hard to maintain 

x = 5  # global variable

def func():
    global x   # by using global keyword we can access global variable
    x = 4  #local variables
    return x

print(x)
print(func())
print(x)