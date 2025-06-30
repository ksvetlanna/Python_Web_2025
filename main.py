# Задача. Ввести список студентов и их средний балл
N = 3
students = []

# упаковали корт еж в список
for _ in range(N):
    student, avarage = input('ФИО: '), float(input('Ср. балл:'))
    students.append((student, avarage))
print(students)

for st in students:
    student, avarage = st
    print('Студент: ',student)
    print('Средний балл: ', avarage)