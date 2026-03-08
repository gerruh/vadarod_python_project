import  random

# 7.1
'''
Создайте 2 кортежа с 10 случайными числами от-5 до 0. Объедините их и посчитайте
сколько раз в получившемся кортеже встретится 0
'''

input_tuple_7_1 = (random.randint(-5, 0), random.randint(-5, 0), random.randint(-5, 0), random.randint(-5, 0), random.randint(-5, 0))
input_tuple_7_2 = (random.randint(-5, 0), random.randint(-5, 0), random.randint(-5, 0), random.randint(-5, 0), random.randint(-5, 0))
output_tuple = input_tuple_7_1 + input_tuple_7_2
print(f'Количество нулей в исходном тюпле: {output_tuple.count(0)}')

# 7.2
'''
Создайте кортеж из 5 случайных чисел от 1 до 10. Все числа, кроме первого и
последнего, распаковать в один список. Для распаковки используйте *
'''
input_tuple_7_2 = (random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10))
first, *middle, last = input_tuple_7_2
output_list_7_2 = list(middle)
print(output_list_7_2)

# 7.3
'''
На вход программе подаются числа. Создайте кортеж из чисел меньше 5.
'''
# Первый вариант с циклом
# input_list_7_3 = list(map(int, input().split('Введите ваш лист чисел: ')))
# for i in input_list_7_3[:]:
#     if i >= 5:
#         input_list_7_3.remove(i)
# print(input_list_7_3)

# Второй вариант с генером
print(tuple((x for x in list(map(int, input('Введите лист чисел: ').split())) if x < 5)))

# 7.4
'''
У вас есть кортеж, который содержит список. Измените кортеж так, чтобы список был
пустым.
'''
input_tuple_7_4 = (1, [1,2,3])
input_tuple_7_4[1].clear()
print(input_tuple_7_4)

# 7.5
'''
Написать задачу с кортежем. Задача должна содержать условие и решение

Пользователь вводит три числа. Создайте кортеж из этих чисел и выведите:

Сумму всех чисел
Минимальное число
Максимальное число
'''
input_tuple_7_5 = (int(input('Введите число 1: ')), int(input('Введите число 2: ')), int(input('Введите число 3: ')))
print(min(input_tuple_7_5))
print(max(input_tuple_7_5))
print(sum(input_tuple_7_5))
