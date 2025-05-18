# algorithm -> method to solve problem in human language

# problem -> find sum of given number
n = input("Enter a number: ")
i, sum = 0, 0
while i < len(n):
    sum += int(n[i])
    i += 1
print(sum)
