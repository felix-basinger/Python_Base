def my_func(arg1, arg2, arg3):
    # a = arg1 + arg2
    # b = arg2 + arg3
    # c = arg1 + arg3
    # return print(f"Sum of the biggest nums = {max(a, b, c)}")

    my_list = [arg1, arg2, arg3]
    my_list.sort()
    my_list.remove(my_list[0])
    result = sum(my_list)
    return print(f"Result of sum {my_list[0]} + {my_list[1]} = {result}")


my_func(int(input("Enter 1 num: ")), int(input("Enter 2 num: ")),
        int(input("Enter 3 num: ")))

