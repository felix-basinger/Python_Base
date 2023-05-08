def div_nums(num_1, num_2):
    if num_1 == 0 or num_2 == 0:
        return print("Error")
    else:
        return print(num_1 / num_2)


div_nums(int(input("Enter num 1: ")), int(input("Enter num 2: ")))
