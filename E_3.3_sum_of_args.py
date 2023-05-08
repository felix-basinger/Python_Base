def my_func(arg1, arg2, arg3):
    a = arg1 + arg2
    b = arg2 + arg3
    c = arg1 + arg3
    return print(f"Sum of the biggest nums = {max(a, b, c)}")


my_func(int(input("Enter 1 num: ")), int(input("Enter 2 num: ")),
        int(input("Enter 3 num: ")))
