# # 6_1
# '''
# Определите сумму элементов, кратных 5, последовательности, заканчивающейся
# числом 0.
# '''
#
# input_list_6_1 = [10,22,30,44,50,0]
# output_int_6_1 = 0
# current_index_6_1 = 0
# while not input_list_6_1[current_index_6_1] == 0:
#     if input_list_6_1[current_index_6_1] % 5 == 0:
#         output_int_6_1 += input_list_6_1[current_index_6_1]
#     current_index_6_1 += 1
# print(output_int_6_1)

# 6_2
# '''
# Определите кол-во отрицательных и положительных элементов последовательности,
# заканчивающейся числом 0.
# '''
# input_list_6_2 = [10,-50,21,-32,0]
# output_int_6_2_positive = 0
# output_int_6_2_negative = 0
# current_index_6_2 = 0
# while not input_list_6_2[current_index_6_2] == 0 :
#     if input_list_6_2[current_index_6_2] > 0 :
#         output_int_6_2_positive += 1
#     elif input_list_6_2[current_index_6_2] < 0 :
#         output_int_6_2_negative += 1
#     else:
#         print(f'Неизвестно куда положить {input_list_6_2[current_index_6_2]}')
#     current_index_6_2 += 1
# print(f'Число положительных элементов оканчивающихся на 0: {output_int_6_2_positive}')
# print(f'Число отрицательных элементов оканчивающихся на 0: {output_int_6_2_negative}')

# 6_3
'''
Вход: целое число N. Определить является ли оно простым. Число называется простым,
если у него есть только 2 делителя: единица и само число N
'''

input_int_6_3 = int(input('Введите целое число: '))
count = 0

for i in range(1, input_int_6_3 + 1):
    if input_int_6_3 % i == 0:
        count += 1

if count == 2:
    print('Число простое')
else:
    print('Число сложное')

# 6_4
'''
Джон пошел в магазин тратить зарплату ZP и покупает все, что попадется под руку.
Напишите программу, которая скажет «Стоп, Джон!» в тот момент, когда, с добавением
нового товара в торзину, итоговая стоимость будет больше ZP . И в конце вывести
сколько денег осталось у Джона.
'''
ZP = float(input("Сколько денег у Джона? "))

total_cost = 0
item_number = 1

while total_cost <= ZP:
    price = int(input(f"Стоимость товара {item_number}: "))

    if total_cost + price > ZP:
        print("Стоп, Джон!")
        break

    total_cost += price
    print(f"Товар {item_number} куплен. Потрачено: {total_cost}")
    item_number += 1

remaining = ZP - total_cost
print(f"У Джона осталось: {remaining}")

# 6_5
'''
Остановить while True
'''
while True:
    print('while True сейчас будет остановлен')
    break