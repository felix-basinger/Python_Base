a = int(input("Enter the number: "))
my_list = [n for n in range(1, a + 1)]


def my_fact(n):
    for el in n:
        yield el


mf = my_fact(my_list)
count = 1
for n in mf:
    if n == len(my_list) + 1:
        break
    else:
        count *= n

b = " * ".join(map(str, my_list))
print(f"{a}! = {b} = {count}")
