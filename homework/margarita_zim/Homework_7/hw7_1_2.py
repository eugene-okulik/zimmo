import random

num = random.randint(1, 10)
print("я загадал число от 1 до 10, попробуй его угадать, у тебя три попытки")

for i in range(1, 4):
    num1 = int(input(f"попытка номер {i}, назови число: "))
    if num1 > num:
        print('попробуй снова, загаданное число меньше')
    elif num1 < num:
        print('попробуй снова, загаданное число больше')
    else:
        print('ура, ты угадал!')
        break
else:
    print(f'попытки закончились, это было число {num}')
