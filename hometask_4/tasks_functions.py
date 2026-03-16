import random


# 13_1
'''
Из полученного списка чисел
создайте список с суммами
этих чисел, отсортированными
по возрастанию
'''


def sum_from_int(nums: list[int]) -> list[int]:
    output_list = []
    for num in nums:
        sum_to_append: int = 0
        num_to_str: str = str(num)
        for i in range(len(num_to_str)):
            sum_to_append += int(num_to_str[i])
        output_list.append(sum_to_append)
        output_list.sort()
    return output_list


test_13_1: list[int] = sum_from_int([113, 220, 3330, 440, 55])
print(test_13_1)

# 13_2
'''
Напишите функцию f(x), которая
возвращает значение следующей
функции, определённой на всей
числовой прямой:
'''


def f(x: int) -> int:
    if not isinstance(x, int):
        raise ValueError(f'{x} не является числом')
    if x <= -2:
        return 1 - pow(x + 2, 2)
    elif -2 <= x <= 2:
        return int(x / 2 - ((x / 2) * 2))
    else:
        return pow(x - 2, 2) + 1


print(f(-10))
print(f(2))
print(f(10))
# print(f('Hello'))

# 13_3
'''
Напишите функцию которая
принимает на вход список
целых чисел, удаляет из него
все нечётные значения, а
чётные нацело делит на два.
'''


def even_nums_only(nums: list[int]) -> list[int]:
    output_list: list[int] = [int(x / 2) for x in nums if x % 2 == 0]
    return output_list


print(even_nums_only([11, 20, 33, 40, 55, 60, 77, 80, 99, 100]))

# 13_4
'''
Напишите функцию, которая
создает список случайных
элементов. На фход функция
принимает кол-во элементов,
минимальное и максимальное
значение
'''


def random_nums_list(num_of_elements: int, min_num: int, max_num: int) -> list[int]:
    output_list: list[int] = [random.randint(min_num, max_num) for _ in range(num_of_elements)]
    return output_list

print(random_nums_list(5, 10, 20))

# 13_6
'''
Напишите функцию,
вычисляющую значение
факториала числа N.
Используйте рекурсию
'''


def factorial(n: int) -> int:
    if n == 0:
        return 1
    return n * factorial(n-1)
print(factorial(5))