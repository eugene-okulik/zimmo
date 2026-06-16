def add_10_to_num(text):
    dv = text.index(': ')
    num_str = text[dv + 2:]
    return int(num_str) + 10


results = [
    'результат операции: 42',
    'результат операции: 54',
    'результат работы программы: 209',
    'результат: 2'
]

for res in results:
    print(add_10_to_num(res))
