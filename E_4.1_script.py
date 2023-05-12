from sys import argv

_, work, salary_in_hour, bonus = argv

print(work)
print(salary_in_hour)
print(bonus)
print((int(work) * int(salary_in_hour)) + int(bonus))
