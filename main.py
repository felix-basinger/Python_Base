# from random import randint
# import My_Func as mf
from sys import argv

#
# mf.hi()
# print(mf.simple())

# length = 10
# my_list = []
# for i in range(length):
#     my_list.append(randint(1, 99))
# print(my_list)
#
# for i in range(length - 1):
#     for j in range(length - i -1):
#         if my_list[j] > my_list[j + 1]:
#             my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
# print(my_list)

# def bubble(array):
#     for i in range(length - 1):
#         for j in range(length - i - 1):
#             if array[j] > array[j + 1]:
#                 temp = array[j]
#                 array[j] = array[j + 1]
#                 array[j + 1] = temp
#
#
# def test(array):
#     size = len(array)
#     for i in range(size - 1):
#         if array[i] > array[i + 1]:
#             return print(False)
#     return print(True)
#
#
# length = 10
# my_list = []
# for i in range(length):
#     my_list.append(randint(1, 99))
#
# print(my_list)
# test(my_list)
# bubble(my_list)
# print(my_list)
# test(my_list)


# i = 0
#
# while True:
#     i += 1
#     if i >= 10:
#         break
#     if i % 2 == 0:
#         continue
#     print(i)

# def my_f(*args):
#     return sum(args)
#
#
# print(my_f(89, 66, 2, 3, 1))
#
#
# def my_fu(**kwargs):
#     return kwargs
#
#
# print(my_fu(n=89, j=66))
#
# my_fun = lambda n1, n2: n1 - n2
#
# print(my_fun(45, 6))
#
# print((lambda a1, a2: a1 - a2)(45, 6))
#
#
# a = [3, 4, 5, 2, 7, 8]
# b = [7, 9, 2, 4, 5, 1]
# c = [5, 7, 3, 4, 5, 9]
#
# dict_a = [{'name': 'python', 'points': 10}, {'name': "java", 'points': 8}]

# print(list(map(lambda x, y, z: x + y + z, a, b, c)))
# print(list(map(lambda x, y, z: 2 * x + 2.5 * y + z, a, b, c)))
# print(list(map(lambda x: x['name'], dict_a)))


# my_list = [12, 3.4, 'str', True, False, [1, 2], 12, 11, 22]

# for i in range(len(my_list)):
# if isinstance(i, list) and 1 in i:
#     if isinstance(my_list[i], int):
#         my_list[i] **= 2
# print(my_list)

# for i, v in enumerate(my_list, 1):
# print(f"{i}) {v}")
# print(my_list)

# n = [1, -10, 13, 4, -8, -21, 34, 9]
# print(n)
# n.sort(reverse=True)
# print(n)
#
# p = (12, 3.4, 'str', True, False, [1, 2], 12, 11, 22)
# print(p)
#
# a = {1, 3, 0, 1, 3, 2}
# print(a)
#
# b = dict(n=3, b=8)
# print(b)
#
# my_dict = {12: 11, 3.4: 22, False: 33, "str": 44, (1, 2): 55, 66: [1, 2]}
# print(my_dict[0])
# print(my_dict[66])
# print(my_dict.keys())
# print(my_dict.items())
# print(my_dict.values())


# name, n_1, n_2, n_3 = argv
# print(argv)
# print(int(n_1) + int(n_2) * int(n_3))


my_list = list(range(1, 11))
new_list = [n + 10 if n % 2 == 0 else n ** 3 for n in my_list]
n_list = [n for n in range(1, 11)]
print(new_list)
print(n_list)

my_dict = {k: n ** 3 for k, n in zip("ASDFGHJCBNM", range(1, 11))}
print(my_dict)