# Дополнительное практическое задание по модулю: "Основные операторы"

number = int(input('Введите число от 3 до 20: '))
result = ''
if 3 < number < 20:
    for i in range(1, number + 1):
        for j in range(i, number + 1):
            if number % (i+j) == 0:
                result += str(i) + str(j)
    print(result)
else:
    print('Вы ввели неверное число')