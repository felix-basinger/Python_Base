#5. Запросите у пользователя значения выручки и издержек фирмы.
#Определите, с каким финансовым результатом работает фирма. Например,
#прибыль — выручка больше издержек, или убыток — издержки больше выручки.
#Выведите соответствующее сообщение.
#Если фирма отработала с прибылью, вычислите рентабельность выручки.
#Это отношение прибыли к выручке. Далее запросите численность
#сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.

profit = int(input("Enter your profit: "))
cost = int(input("Enter your cost: "))
workers = int(input("Enter count of workers: "))

result = (profit - cost)
if result > 0:
    print(f"{result} // Profit > cost")
    profitX2 = (profit / result) * 100
    print(f"{profitX2:.1f}")
    print(f"{(profit / workers):.2f} ")
elif result == 0:
    print("Result = cost")
else:
    print(f"{result}Result < cost")


