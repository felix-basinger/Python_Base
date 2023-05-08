def my_func(x, y):
    # return print(x ** y)
    result = 0
    i = 0
    while i < abs(y):
        result += 1 / x
        i += 1
    return print(round(result, 2))


my_func(float(input("Enter your 1 num: ")), int(input("Enter your 2 num: ")))
