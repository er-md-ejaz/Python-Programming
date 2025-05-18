#* sum of numbers using 1 to 10

n = int(input("Enter number: "))
i, total = 1, 0
while i <= n:
    total += i
    i += 1
print(total)