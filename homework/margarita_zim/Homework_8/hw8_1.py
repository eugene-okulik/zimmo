import random

salary = int(input("Напишите, какая у вас зарплата в долларах? "))
bonus = random.choice([True, False])
random_bonus =  random.randint(1, 100)

if bonus == True:
    total_salary = salary + random_bonus
else:
    total_salary = salary

print(f'{salary}, {bonus} - ${total_salary}')
