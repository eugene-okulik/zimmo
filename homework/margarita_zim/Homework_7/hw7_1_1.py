import random

num = random.randint(1, 20)
print("я загадал число от 1 до 20, попробуй его угадать")

while True:
    num1 = int(input("назови число: "))
    if num1 > num:
        print('попробуй снова, загаданное число меньше')
    elif num1 < num:
        print('попробуй снова, загаданное число больше')
    else:
        print('ура, ты угадал!')
        break
