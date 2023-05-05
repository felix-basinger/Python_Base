a = int(input("Enter your current result: "))
b = int(input("Enter your desired result: "))
count = 2
print(f"1 day: {a}")

while a < b:
    a += a * 0.1
    print(f"{count} day: {a:.2f}")
    count += 1