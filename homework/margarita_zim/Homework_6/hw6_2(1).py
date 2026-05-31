# способ 1
digits = list(range(1, 101))
for digit in digits:
    n = ""
    if digit % 3 == 0:
        n += "Fuzz"
    if digit % 5 == 0:
        n += "Buzz"
    if not n:
        n += str(digit)
    print(n)

