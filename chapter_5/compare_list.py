# '==' checks does both list are same or not 
# while "is" checks does both list are present at same memory place or not

fruits1 = ['apple', 'banana', 'orange']
fruits2 = ["banana", "apple", 'orange']
fruits3 = ['pineapple', 'mango', 'grapes']
fruits4 = ['apple', 'banana', 'orange']
# print(fruits1 == fruits2)
print(fruits1 == fruits4)
print(fruits1 is fruits4)