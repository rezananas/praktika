# Самостоятельная работа по уроку "Распаковка позиционных параметров".

def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(5)
print_params(5, 'столбец')
print_params(5, 'столбец',False)
print_params(b=25)
print_params(c=[1,2,3])

values_list = [2, 'литота', True]
values_dict = {'a': 3, 'b': 'гипербола', 'c': False}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
