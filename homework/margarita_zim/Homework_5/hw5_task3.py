students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

# распаковываем списки
students = ", ".join(students)
subjects = ", ".join(subjects)

print(f"Students {students} study these subjects: {subjects}")