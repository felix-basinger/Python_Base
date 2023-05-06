my_str = input("Enter your string: ")
print(my_str)
my_list = list(my_str)
print(my_list)

count = 1
n = 0
i = 0
while i < len(my_list):
    if my_list[i] == " " or my_list[i] == "." or my_list[i] == "," or i + 1 == len(my_list):
        a = "".join(my_list[n:i + 1])
        if len(a) > 10:
            print(f"{count}) " + a[0:10])
            n = i + 1
            i += 1
            count += 1
        else:
            print(f"{count}) " + "".join(my_list[n:i + 1]))
            n = i + 1
            i += 1
            count += 1
    else:
        i += 1
