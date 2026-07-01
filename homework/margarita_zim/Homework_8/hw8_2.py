def num_fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib_gen = num_fibonacci()


def get_nth_fib(n):
    fib = num_fibonacci()
    for _ in range(n):
        next(fib)
    return next(fib)


num_5 = get_nth_fib(4)
num_200 = get_nth_fib(199)
num_1000 = get_nth_fib(999)
num_100000 = get_nth_fib(99999)

print(num_5)
print(num_200)
print(num_1000)
print(num_100000)
