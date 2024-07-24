# Домашняя работа по уроку "Пространство имён"

calls = 0
def count_calls(call):
    global calls
    calls += call
    return calls

def string_info(string):
    list1 = []
    list1.append(len(string))
    list1.append(string.upper())
    list1.append(string.lower())
    count_calls(1)
    return list1

def is_contains(string, list_to_search):
    string.lower()
    list2 = []
    count_calls(1)
    for i in list_to_search:
        list2.append(i.lower())
    return (string.lower() in list2)

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)