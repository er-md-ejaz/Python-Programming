def fibonacci_series(n):
    a = 0
    b = 1
    if n==1:
        print(a, end=" ")
    elif n==2:
        print(a, b)
    else:
        print(a,b, end=" ")
        for i in range(n-2):
            c = a + b
            a = b
            b = c
            print(b, end=" ")


n = int(input("How many terms do you want to print: "))
fibonacci_series(n)