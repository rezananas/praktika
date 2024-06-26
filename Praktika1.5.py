# Практическое задание по теме: "Неизменяемые и изменяемые объекты. Кортежи"

immutable_var = 1, 2, 3, True, 'Байкал'
print('Immutable tuple:', immutable_var)

# immutable_var[0] = 5
# print(immutable_var)
# Кортеж - это НЕИЗМЕНЯЕМЫЙ список

mutable_list = [1, 2, 3, True, 'Байкал']
mutable_list.append('Эльбрус')
print('Mutable list:', mutable_list)
mutable_list.extend('Сочи')
print('Mutable list:', mutable_list)
mutable_list.extend(['Сочи', 5])
print('Mutable list:', mutable_list)
mutable_list.remove('Сочи')
print('Mutable list:', mutable_list)
