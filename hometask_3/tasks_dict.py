# # 8.1
# '''
# Создайте словарь person, в котором будут ключи name, age, city. Выведите значение
# возраста.
# '''
# person = {'age': 23,'city': 'Minsk'}
# print(person['age'])
#
# # 8.2
# '''
# Программа принимает список из трех слов. Создать словарь, в котором ключ — слово,
# значение — количество символов в слове
# '''
# words_length_dict = {x:len(x) for x in input().split()}
# print(words_length_dict)
#
# # 8.3
# '''
# На вход подается список чисел. Создать словарь, в котором ключ — число, значение —
# число на 10% больше. Значение должно быть округленное.
# '''
# nums_dict = {x:int(x*1.1) for x in list(map(int,input().split()))}
# print(nums_dict)

# # 8.4
# '''
# Создайте следующий словарь: ключи – BMW, Tesla; значения – список из 3х моделей.
# Выведите 1ое и последнее значения каждого из ключей.
# '''
# cars_dict = {'BMW': ['M3', 'M1', 'X7'], 'Tesla': ['Model X', 'Model Y', 'Model 3']}
# for key,value in cars_dict.items():
#     print(f'Первая и последняя модель {key}: первая - {value[0]}, последняя: {value[len(value)-1]}')

# # 8.5
# '''
# Написать задачу со словарем. Задача должна содержать условие и решение
#
# Удали всё из словаря принтуя что удаляешь
# '''
# deletion_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
# for i in range(len(deletion_dict)):
#     popped_item = deletion_dict.popitem()
#     print(f'Сейчас я удалю значение {popped_item[1]} по ключу {popped_item[0]}')

# 8.6
# '''
# Создать словарь, который в качестве ключа будет использовать страну, а в качестве
# значения - ее столицу. Внеси в него следующие страны: Россия (Москва), Украина
# (Киев), Италия (Рим), Испания (Мадрид), Болгария (София).
# Программа должна запрашивать у пользователя, столицу какой страны он хочет узнать
# и выдавать результат.
# '''
# countries_dict = {'Россия': 'Москва', 'Украина': 'Киев', 'Италия': 'Рим', 'Испания': 'Мадрид', 'Болгария': 'София'}
# capital_str_input = input('Столицу какой страны вы хотите узнать: ')
#
# if capital_str_input in countries_dict:
#     print(f'Столица страны {capital_str_input} - {countries_dict[capital_str_input]}')
# else:
#     print(f'Нет информации касательно столицы страны {capital_str_input}')

# 8.7
'''
Создать словарь, ключи — числа, значения — слова. Удалить из него все
пары с нечетными ключами. Вывести на печать
В этом вам может помочь статья, что сбрасывала ранее.
'''
input_dict = {1:'Вода', 2: 'Огонь', 3: 'Земля', 4: 'Воздух'}
remove_list = []
for key, value in input_dict.items():
    if not key%2 == 0:
        remove_list.append(key)

for item in remove_list:
    input_dict.pop(item)

print(input_dict)

# 8.8
'''
Написать задачу со словарем и циклом.
Представление: условия и решение.

Поменяй ключи и значения местами пользуясь циклами
'''
dict_to_reverse = {1:'Hi', 2:'Hola', 3: 'Привет'}
keys_list = list(dict_to_reverse.values())
values_list = list(dict_to_reverse.keys())
output_dict = {}

for i in range(len(keys_list)):
    output_dict[keys_list[i]] = values_list[i]
print(output_dict)
