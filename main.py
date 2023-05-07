from random import randint


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

def bubble(array):
    for i in range(length - 1):
        for j in range(length - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp


def test(array):
    size = len(array)
    for i in range(size - 1):
        if array[i] > array[i + 1]:
            return print(False)
    return print(True)


length = 10
my_list = []
for i in range(length):
    my_list.append(randint(1, 99))

print(my_list)
test(my_list)
bubble(my_list)
print(my_list)
test(my_list)

# i = 0
#
# while True:
#     i += 1
#     if i >= 10:
#         break
#     if i % 2 == 0:
#         continue
#     print(i)


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
