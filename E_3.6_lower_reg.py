def int_func(stroke):
    s = []
    b = stroke.split()
    for i in b:
        n = i.capitalize()
        s.append(n)
    return print(' '.join(s))


int_func(input())
