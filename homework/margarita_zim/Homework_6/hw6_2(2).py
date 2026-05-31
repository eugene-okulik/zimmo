# способ 2
digits = list(range(1, 101))
for digit in digits:
    if digit % 15 == 0:
        print("FuzzBuzz")
    elif digit % 3 == 0:
        print("Fuzz")
    elif digit % 5 == 0:
        print("Buzz")
    else:
        print(digit)
