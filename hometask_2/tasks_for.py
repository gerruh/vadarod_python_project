# # 5_1
# '''
# Программа перемножает все нечетные значения от 1 до 10 включительно
# '''
#
# result_int_5_1 = 0
# for i in range(1,11):
#     if i == 1:
#         result_int_5_1 = i
#         continue
#
#     if not i%2==0:
#         print(f'Сколько есть сейчас: {result_int_5_1}, на сколько умножится: {i}')
#         result_int_5_1 *= i
#
# print(result_int_5_1)
#
# # 5_2
# '''
# Вход: целое число до 15. Программа выводит лесенку из чисел
# '''
#
# input_int_5_2 = int(input('Введите число: '))
# for i in range(1,input_int_5_2+1):
#     iteration_list = [x for x in range(1,i+1)]
#     print(' '.join(map(str, iteration_list)))

# 5_3
'''
Переписать задачи 5.4, 5.5., 5.7, чтобы на вход получался список с использованием
генератора списков
'''
# # 5_3_4
# '''
# Вход: 2 числа a и b
# Программа выводит все
# числа от a до b
# включительно.
# Числа могут быть любыми
# и подаваться в любом
# порядке.
# '''
# input_num_list_5_3_4 = [x for x in range(int(input('Введите число а: ')),int(input('Введите число b: '))+1)]
# print(input_num_list_5_3_4)
#
# # 5_3_5
# '''
# Вход: 2 числа a и b
# Программа выводит все четные
# числа на промежутке от a до b
# '''
# input_num_list_5_3_5 = [x for x in range(int(input('Введите число а: ')),int(input('Введите число b: '))+1) if x%2==0]
# print(input_num_list_5_3_5)

# # 5_3_7
# '''
# Вход: строка
# Программа выводит
# каждый символ строки 2
# раза
# '''
# input_num_list_5_3_7 = [x*2 for x in list(input('Введите строку: '))]
# print(input_num_list_5_3_7)

# 5_5
'''
Удалять из списка нечётные числа по индексу
'''

input_list_5_5 = [x for x in range(1,11)]
indexes_to_go_list = list()
for index,item in enumerate(input_list_5_5):
    if not item%2==0:
        indexes_to_go_list.append(index)

for i in reversed(indexes_to_go_list):
    del input_list_5_5[i]

print(indexes_to_go_list)
print(input_list_5_5)