
while True:
    c = input("Enter your operation: ")
    if c == "0":
        break
    if c in ('+', "-", "*", "/"):
        a = float(input("Enter 1 num: "))
        b = float(input("Enter 2 num: "))
        if c == "+":
            print(a + b)
        elif c == "-":
            print(a - b)
        elif c == "*":
            print(a * b)
        elif c == "/":
            if c != 0:
                print(a / b)
            else:
                print("error")
    else:
        print("ERROR")
