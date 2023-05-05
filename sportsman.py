a = int(input("Enter your current result: "))
b = int(input("Enter your desired result: "))
count = 1

while a < b:
    a += a * 0.1
    print(f"{count} day: {a:.2f}")
    count += 1