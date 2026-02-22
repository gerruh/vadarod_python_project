# 4.1
'''
Вход: число. Программа выводит сообщение положительное это число или
отрицательное
'''

num_input = int(input('Введите число: '))

if num_input >= 0:
    print(f'Number {num_input} is positive')
else:
        print(f'Number {num_input} is negative')

# 4.2
'''
Вход: температура и вид градусов. Программа переводит из Цельсия в Фаренгейты и
наоборот.

F = Фаренгейт
C = Градус
'''

temp_input = int(input('Введите кол-во градусов: '))
temp_type_input = input('Введите систему измерения градусов: ')

if temp_type_input == 'F':
    print(f'{temp_input} фаренгейтов в градусах: {(temp_input - 32) + 1.8}')
elif temp_type_input == 'C':
    print(f'{temp_input} градусов в фаренгейтах = {(temp_input * 1.8) + 32}')
else:
    print(f'Неизвестный тип градусов {temp_type_input} в количестве {temp_input}')

# 4.3
'''
Написать простой калькулятор: сложение, вычитание, деление, умножение. Программа
в зависимости от действия с двумя введенными пользователем числами выводит
результат.
'''

operable = True

while operable:
    first_value_input = int(input('Введите первое число: '))
    second_value_input = int(input('Введите второе число: '))
    operation_type_input = input('Введите тип операции: ')

    match operation_type_input:
        case '+':
            print(f'Сложение: {first_value_input + second_value_input}')
        case '-':
            print(f'Вычитание: {first_value_input - second_value_input}')

        case '*':
            print(f'Умножение: {first_value_input * second_value_input}')

        case '/':
            print(f'Деление: {first_value_input / second_value_input}')

        case _:
            print(f'Я не знаю как обработать числа {first_value_input} и {second_value_input} c типом операции {operation_type_input}')
            operable = False

# 4.4
'''
Вход: 2 слова. Программа проверяет являются ли они анаграммой (из одного слова
можно составить другое). Если да – вывести ‘anagram’, если нет – ‘just words’.
Sorted(variable)
'''

str_input_1 = input('Введите первое слово: ')
str_input_2 = input('Введите второе слово: ')

if sorted(str_input_1) == sorted(str_input_2):
    print('Слово явялется анаграммой')
else:
    print('Слово не является анаграммой')

# 4.5
'''
Придумать задачу для условий. Использовать метод строк или списков или оба. Задача
должна содержать условие и Ваше решение.

Обрезать строку от пробелов всеми способами
'''

str_unstripped_input = input('Введите строку с пробелами в начале и в конце: ')
print(f'С обоих сторон: {str_unstripped_input.strip()}')
print(f'Справа: {str_unstripped_input.rstrip()}')
print(f'Слева: {str_unstripped_input.lstrip()}')