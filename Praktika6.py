# Практическое задание по теме: "Словари и множества"

my_dict = {'Настя' : 1997, 'Рома' : 2005}
print(my_dict)
print(my_dict['Настя'])
print(my_dict.get('Оля'))
my_dict.update({'Дима' : 1969, 'Тамара' : 1933})
print(my_dict.pop('Тамара'))
print(my_dict)

my_set = {1, 2, 3, 3, 2, 1, True, 'Кикимора', (1, 2, 3)}
my_set = set(my_set)
print(my_set)
my_set.add(5)
my_set.add('Оригами')
my_set.discard(1)
print(my_set)