while True:
    b = int(input("Play? Enter any num for play and 0 for exit: "))
    if b == 0:
        break
    else:
        num = int(input("Enter your num: "))
        my_list = [7, 5, 3, 3, 2]
        for i in range(len(my_list)):
            if num > my_list[0]:
                my_list.insert(my_list.index(my_list[i]), num)
                break
            elif num < my_list[-1]:
                my_list.append(num)
            elif num < my_list[i]:
                continue
            else:
                my_list.insert(my_list.index(my_list[i]), num)
                break
    print(my_list)
