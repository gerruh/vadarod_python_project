# 10.7
'''
Пользователь вводит слова.
Записать их в файл: каждое
слово на отдельной строке
'''

str_input_list = input('Введите слова: ').split()

try:
    with open('temp_file.txt', 'w') as f:
        for item in str_input_list:
            f.write(f'{item}\n')
except FileNotFoundError:
    print('Файл не найден')
try:
    with open('temp_file.txt', 'r') as f:
        print(f.read())
except FileNotFoundError:
    print('Файл не найден')

# 10.8
'''
Дан список [5, True, ‘abc’].
Записать его в файл
'''

append_list = [5, True, 'abc']

with open('temp_file.txt', 'w') as f:
    for item in append_list:
        f.write(f'{item}\n')

# 10.9
'''
Создать список чисел. Записать
каждое нечетное число в файл
'''
int_input_list = list(map(int, input('Введите числа').split()))
with open('temp_file.txt', 'w') as f:
    for item in int_input_list:
        if item%2 != 0:
            f.write(f'{item}\n')

with open('temp_file.txt', 'r') as f:
    print(f.read())