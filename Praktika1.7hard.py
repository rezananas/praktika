# Дополнительное практическое задание по модулю
# Задание "Средний балл":
# Вам необходимо решить задачу из реальной жизни:
# "школьные учителя устали подсчитывать вручную средний балл каждого ученика,
# поэтому вам предстоит автоматизировать этот процесс":

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list = list(students)
students_list.sort()
print(students_list)

a = grades.pop(0)
sum_a = 0
for i in a:
    sum_a += i
average_a = sum_a / len(a)
print(average_a)

b = grades.pop(0)
sum_b = 0
for i in b:
    sum_b += i
average_b = sum_b / len(b)
print(average_b)

c = grades.pop(0)
sum_c = 0
for i in c:
    sum_c += i
average_c = sum_c / len(c)
print(average_c)

d = grades.pop(0)
sum_d = 0
for i in d:
    sum_d += i
average_d = sum_d / len(d)
print(average_d)

e = grades.pop(0)
sum_e = 0
for i in e:
    sum_e += i
average_e = sum_e / len(e)
print(average_e)

dict = {students_list[0] : average_a,
        students_list[1] : average_b,
        students_list[2] : average_c,
        students_list[3] : average_d,
        students_list[4] : average_e}
print(dict)
