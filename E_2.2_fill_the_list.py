my_list = []
length = int(input("Enter length of your list: "))
count = 1

for i in range(length):
    elem = input(f"Enter {count} elems of your list: ")
    my_list.append(elem)
    count += 1
print(my_list)

i = 0
while i < len(my_list):
    if i >= len(my_list) - 1:
        break
    else:
        if len(my_list) % 2 == 0:
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
            i += 2
        else:
            while i < len(my_list) - 1:
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
                i += 2
print(my_list)
