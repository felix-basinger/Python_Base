from functools import reduce

my_list = [n for n in range(100, 1001) if n % 2 == 0]
print(my_list)


def my_func(el_1, el_2):
    return el_1 * el_2


print(reduce(my_func, my_list))
