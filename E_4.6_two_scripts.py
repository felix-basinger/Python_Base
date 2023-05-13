from itertools import count, cycle

a = int(input("Enter a: "))
b = int(input("Enter b: "))

for n in count(a):
    if n == b:
        break
    elif a > b:
        print("Error")
        break
    else:
        print(n)


count = 0
for i in cycle([1, 2, 3]):
    if count > 10:
        break
    print(i)
    count += 1
