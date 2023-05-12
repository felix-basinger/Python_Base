my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
my_list.sort()
print(my_list)

for i in range(len(my_list)):
    if i == len(my_list) - 1:
        break
    else:
        new_list = [my_list[i] for i in range(len(my_list) - 1) if
                    my_list[i] != my_list[i + 1] and my_list[i] != my_list[i - 1]]
        print(new_list)
        break
