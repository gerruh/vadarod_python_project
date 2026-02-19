# 2.1
'''
Дана строка 'rythm rough rush shake than’. Программа удаляет все буквы «а» в строке и
полсчитывает кол-во уждаленных символов.
'''
input_string_2_1 = 'rythm rough rush shake than'
print(f' В {input_string_2_1} было {input_string_2_1.count('a') } букв а, теперь это {input_string_2_1.replace('a', '')}')

# 2.2
'''
Дана строка 'rythm (rough rush shake) than’. Программа выводит только ту часть строки,
которая НЕ в скобочках.
'''
input_string_2_2 = 'rythm (rough rush shake) than'
print(f'До:{input_string_2_2[:6]}, После:{input_string_2_2[24:]}')

# 2.3
'''
Дана строка 'rythm rough rush shake than’. Программа считает сколько букв ‘t’ в строке.
'''
input_string_2_3 = 'rythm rough rush shake than'
print(f' Кол-во букв t: {input_string_2_3.count('t')}')

# 2.4
'''
Дана строка 'rythm rough rush shake than’. Программа выводит строку, в которой
последовательность символов между перым и последним появлением буквы ‘h’
повернута в противоположном порядке
'''
input_string_2_4 = 'rythm rough rush shake than'
print(f'{input_string_2_4[input_string_2_4.find('h')+1:input_string_2_4.rfind('h')][::-1]}')

# 2.5
'''
Дана строка 'rythm rough rush shake than’. Программа выводит строку, в которой все
буквы ‘h’ заменены на ‘H’, кроме первого и последнего вхождений.
'''
input_string_2_5 = 'rythm rough rush shake than'
print(f'{input_string_2_5[:4] + input_string_2_5[4:].replace('h','H',input_string_2_5.count('h') - 2)}')