my_dict = {
  "tuple": (70, 24, 'name', 0, -8, 'number'),
  "list": [90, 'text', 1, 'surname', 314, -2],
  "dict": {'country': 'China',
           'capital': 'Beijing',
           'language': 'Chinese',
           'population, bil.': 1.4,
           'currency': 'Chinese yuan(RMB)'
           },
  "set": {1, 5, 7, 5, 'word', 'file', 9}
}
# Для того, что хранится под ключом ‘tuple’: выводим на экран последний элемент
print(my_dict['tuple'][-1])

# Для того, что хранится под ключом ‘list’: добавляем в конец списка еще 1 элемент,
# удаляем второй элемент списка
my_dict['list'].append('stop')
my_dict['list'].pop(1)

# Для того, что хранится под ключом ‘dict’:
# добавляем элемент с ключом ('i am a tuple') и любым значением, удаляем какой-нибудь элемент
my_dict['dict']['i am a tuple'] = "and it's ok"
my_dict['dict'].pop('currency')

# Для того, что хранится под ключом ‘set’: добавляем новый элемент в множество,
# удаляем элемент из множества
my_dict['set'].add(2026)
my_dict['set'].remove(1)

print(my_dict)
