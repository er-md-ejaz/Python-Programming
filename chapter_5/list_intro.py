# list -> ordered collection of items
# we can store anything in list e.g. int, float, string and mixed also
# and indexing is same as string and we can do slicing as well 


numbers = [1,2,4,3,2]
print(numbers)
print(numbers[2])

words = ['md', "ejaz", "ansari"]
print(words)
print(words[:2])

mixed = [1, 4, 2.5, 3.9, "ansari", 'sjsi']
print(mixed)
print(mixed[-1])

mixed[1] = 'four'
print(mixed)

mixed[1:3] = "two"
print(mixed)
mixed[1:2] = ['one', "two", 'three', 'four']
print(mixed)
