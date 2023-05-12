from random import randint

my_list = [randint(-50, 50) for el in range(randint(10, 20))]
print(my_list)
for n in my_list:
    if n == len(my_list) - 1:
        break
    else:
        new_list = [my_list[n + 1] for n in range(len(my_list) - 1) if my_list[n] < my_list[n + 1]]
        print(new_list)
        break


