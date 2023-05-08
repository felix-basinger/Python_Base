my_list = [12, 34.5, False, [1, 3, 5], (3, 5, 6), {'r': 3, 'n': 5}, b'text', "rat"]

for i, v in enumerate(my_list, 1):
    print(f'{i}) {v} - {type(v)}')

