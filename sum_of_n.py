n = int(input("Enter your num: "))

if 0 < n < 10:
    a = (n * 10) + n
    b = (n * 100) + ((n * 10) + n)
    result = n + a + b
    print(f"{n} + {a} + {b} = {result}")
elif 10 <= n < 100:
    a = (n * 100) + n
    b = (n * 10000) + ((n * 100) + n)
    result = n + a + b
    print(f"{n} + {a} + {b} = {result}")
elif 100 <= n < 1000:
    a = (n * 1000) + n
    b = (n * 1000000) + ((n * 1000) + n)
    result = n + a + b
    print(f"{n} + {a} + {b} = {result}")
else:
    print("Incorrect value")