# name = 'Alexandr'
#
# print('Hello,', name)

# print(2 + 4)
# print('Hello')
#
# if 1<2:
#     print('Hello')

# if 1 > 2:
#     print('hello')
#     print(2+3)
# else:
#     print('sosi syka')

# print('Hello students') #это комментарии
#
# print('Hello world') # TODO: Изменить текст сообщения
# print(1+2) # TODO: изменить

# print('hello world!')   # TODO: тут комментарий
#
# print(1+3)  # TODO: изменить на имя пользователя
#             # на переменные

# a = 5
# b = 4
# id(a)
# print(id(b))
# print(id(a))
# a = b
# print(id(b))

# a = 93
# b = 2.5
# c = "My first program"
# print(id(a))
# print(id(b))
# print(id(c))
# print(type(a))
# print(type(b))
# print(type(c))
# a = 2.5
# print(id(a))
#
# x = y = z = 138
# print(id(x))
# print(id(y))
# print(id(z))

# my_none_variable = None
# print(id(my_none_variable))

# a = 7 == 7
# print(a)
# a = 5
# b = 3
# c = 1
# z = a - b == 2 or c + b === 4
# print(z)

# z = 5-3 ==2 or 1+3 == 4
# print(type(z))
# print(id(z))

"""
Укажите значения логических переменных А и В, при которых значение логического
выражения НЕ (НЕ А ИЛИ В) будет истинным.

А       В       НЕ А        НЕ А или В
0       0
0       1
1       0
1       1

"""

#  Найдите значения выражений:

# f1 = (0 or 1) and (0 or 1)
# print('f1 =', f1)
#
# f2 = 0 or 1 and 0 or 1
# print('f2 =', f2)
#
# a = 0
# b = 0
# f3 = (a or 1) or (b and 0)
# print('f3 =', f3)

# f1 = (not 1 or 1) and not 0 or 0
# print('f1 =', f1)
#
# f2 = (not 0 and 1) or (not 1 and 1)
# print('f2 = ', f2)
#
# f3 = not 1 or 0 or (0 and 1)
# print('f3 =', f3)


# А - Брюнет
# В - Усами not B - без усов
# С - Блондин
# D - с портфелем not D - без портфелем
# Е - Шатен

# A = 0
# B = 1
# C = 1
# D = 1
# E = 0
#
#
# f1 = (not A and B) or (A and not B)
# f2 = (not C and not B) or(C and B)
# f3 = (not C and not D) or (C and D)
# f4 = (not E and D) or (E and not D)
#
# f5 = (A and not C and not E) or (not A and C and not E) or (not A and not C and E)
#
# f = f1 and f2 and f3 and f4 and f5
# print('f=', f)
#
# # А - Брюнет
# # В - Усами not B - без усов
# # С - Блондин
# # D - с портфелем not D - без портфелем
# # Е - Шатен
#
# (not K or M) or (not L or M or N)

# number = 10
# number += 5
# print(number)
# number -= 3
# print(number)
# number **= 2
# print(number)
# number /= 2
# print(number)
# number += 23
# print(number)

# first_num = "2"
# second_num = 3
# third_num = int(first_num) + second_num
# print(third_num)

# a = 2.34212
# b = 0.1231
# c = a + b
# print(round(c,10))

# x = 0b101
# print(x)
#
# a = 0o11
# print(a)
#
# y = 0x0a
# print(y)
#
# z = x + y
# print(z)

# x = 3
# y = 2
# print(pow(x,y))
# import math
# a = 144
# print(sqrt(a))

# a = [1,2,3,4,5]
# print(list(a))
# b = 'America'
# print(list(b))

# c = [c*3 for c in 'LIST']
# print(c)

# my_list = [True, 786, 3.14, 'text']
# print(my_list[::-2])

# a = [-1, 1, 66.25, 333, 333,123, 'text', True]
# a.insert(1, x)
# print(a)

# l = [12,123,5,76,8,]
# a = l.pop(3)
# print(a)
#
# list = ['list', True, False, 3, 3.424]
# b = list.pop(3)
# print(b)
#
# print(l)
# print(list)

# list1 = [1,2,3,4,5,6,7]
# print(list1[1])
# print(list1[2])
# print(list1[3])
# print(list1[4])
# print(list1[5])

# print(list1[-1: 2])

# a = count(list1)
# print(a)


# a = [1,2,3,4,5]
# b = a.reverse()
# print(b)

# fruits = [12,3,4,5,6]
# fruits.count(1)

# mylist = [10,11,12,13,14,15]
# print("mylist before reverser:", mylist)
# mylist.reverse()
# print("mylist after reverse:", mylist)
#
# a = [1,2,3,4,5]
# a.reverse()
# print(a)
#
# b = ["after to night", True, 4, 6.45, False]
# b.reverse()
# print(b)

# x = [1,2,3,4,5]
# x1 = x[-4]
# print(x1)
#
# fruits = ['banana', 'orange', 'pear', 'apple', 'pineapple']
# fruits.reverse()
# print(fruits)
# fruits.append('grape')
# print(fruits)
# fruits.sort()
# print(fruits)

# my_tuple = (True, 786, 4.1354, 'text')
# second_tuple = [123,'text1']
# print(my_tuple)
# print(my_tuple[0])
# print(my_tuple*3)
# print(my_tuple+my_tuple)
# print(my_tuple+second_tuple)
# print(my_tuple[1] = 4)

# my_tuple = (786,3.14,'text',)
# a,b,c = my_tuple
# print(a)
# print(b)
# print(c)

# print(list(range(10)))
# print(list(range(0,30,5)))
# print(list(range(0,10,3)))
# print(list(range(0, -10, -1)))


# my_list1 = [123,'text']
# print(123 in my_list1)
# print('text' in my_list1)
# print('text' not in my_list1)
# print(4 in my_list1)
#
# print(len(my_list1))

# myList = [1,2,3,4,5,6,7,8,9]
# print(max(myList))
# print(min(myList))
# print(sum(myList))
# print(sorted(myList, reverse=True))
# my_list2 = ['banana', 'apple', 'pear', 'cucumber', 'gear']
# print(sorted(my_list2, reverse=False))
# myList.count(23)
# print(myList)

# my_list1 = [1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0]
# sum_1 = sum(my_list1)
# print('Сумма равна:', sum_1)
#
# my_list2 = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
# sum_2 = sum(my_list2)
# print('Сумма равно:', sum_2)
#
#
# my_list3 = [10,20,30,40,50,60,70,80,90,100,0,1,2,3,4,5,6,7,8,9]
# sum_l = sum(my_list3)
# print('Сумма:', sum_l)

# May_temperature = [20,25,30,-4,22,34,21,29,27,-4,21,4,23,27,
#                    18,15,13,12,10,11,9,8,7,5,3,2,32,21,18,-14,35]
# # print(len(May_temperature))
# # print(max(May_temperature))
# # print(min(May_temperature))
#
# May_t = max(May_temperature)
# Min_t = min(May_temperature)
# Len_1 = len(May_temperature)
# index_max_t = May_temperature.index(May_t)+1
# index_min_t = May_temperature.index(Min_t)+1
# print('Максимальная температура в Май месяце:', May_t)
# print('Минимальная температура в Май месяце:', Min_t)
# print('Количество дней в Мае месяце:', Len_1)
# print('День когда была максимальная температура:', index_max_t)
# print('День когда была самая низкая температура:', index_min_t)

# my_list1 = [3,2,4,6,2,1,10,-8,-5,]
# my_list1.reverse()
# print(my_list1)
# my_list1.sort()
# print(my_list1)

# my_sort = sorted(my_list1)
# print(my_sort)

# my_list1.sort()
# print(my_list1)

# my_list1.sort(reverse=True)
# print(my_list1)

# my_list1 = [3,2,4,-1,5,9,50,51]
#
# max_list = max(my_list1)
# print('Максимальное значение равно:', max_list)
#
# my_list1.remove(max_list)
# print(my_list1)
#
# my_list1.insert(0,max_list)
# print(my_list1)

# my_sort = sorted(my_list)
# print(my_sort)
# my_sort.reverse()
# print(my_sort )

# min_list = min(my_list)
# print(min_list)
# my_list.remove([0])
# print(my_list)

# min_list = min(my_list)
# print('Минимальное значение равно:', min_list)
#
# ind_minimal = my_list.index(min_list)
# print('Индекс минимального значение равно:' , ind_minimal)
#
# del my_list[0:ind_minimal]
# print(my_list)


# my_list = [4,3,-5,-1,-59, 1,2,-2,5,-4, -55]
# max_element = max(my_list)
# print(max_element)
# index_max_element = my_list.index(max_element)
# print(index_max_element)
#
# del my_list[9:]
# print(my_list)


# text = 'Hello, Python!'
#
# print(text[::-1])
# print('o' in text)
# print('P' in text)
# print('p' in text)
# print(',' in text)
# print('H' in text)
# print('h' in text)
# print('E' in text)

# text_1 = 'Hello, Natalya, '
# text_2 = 'nice to code you'
# print(text_1 + text_2)
#
# print(text_1*2)
# print(text_2[-1]*10)
# print(len(text_2))
# print(max(text_2))
# print(text_2.count(text_2))


# a = ['hey', 1, 4.3, ['nested'], 1, {1:3}]
# print(a.count({1:3},))
# print(a.count(['nested']))
# print(a.count(5))
# text1 = 123
# text = 'Hello, Python123!'
# print(text.count("1"))
# print(text1.count(2))

# text_1 = 'hi, everyone!'
# a = text_1.capitalize()
# print(a)
#
# text_2 = 'Kololololo'
# x = text_2.count('l')
# print(x)
# print(x)

# text = 'Hello, Python!'
# print(text.endswith("on!"))
# print(text.endswith("!"))
# print(text.endswith("asf"))
# print(text.startswith('Hello'))
# print(text.startswith('hello'))

# a = 'ds\tdsf\123'
# a.expandtabs()
# print(a)

# s = 'Kolololo'
# print(s.find('olo'))
# print(s.find('lo',3))


# a = " ".join(['aaa','bbb', 'ccc'])
# print(a)
# b = "_".join(['aaa', 'bbb', 'ccc'])
# print(b)
# c = "+++".join(['aaa', 'bbb', 'ccc'])
# print(c)

# a = '42'.ljust(5)
# print(a)
#
# b = "36: ".ljust(7, "+")
# print(b)
#
# c = ':text1'.rjust(10, "-")
# print(c)
#
# z = '-43'.zfill(5)
# print(z)

# a = '    spacious   '.lstrip()
# print(a)
#
# b = 'www.example.com'.lstrip('cmowz.')
# print(b)

# a = 'text'.split(',', maxsplit=2)
# print(a)

# a = 'Text'.swapcase()
# print(a)
#
# b = 'Hello, Queen!'.swapcase()
# print(b)
#
# a = 'Hello, Python!'.encode()
# print(a)
#
# b = '123'.encode()
# print(b)

# s = 'Еживику для ежат \
#      Принесли два ежа. \
#      Ежевику еле-еле \
#      Ежата возле ели съели.'
#
# count_E = s.count('Е')
# print(count_E)
# count_e = s.count('е')
# print(count_e)
# print(len(s))
# count_res = count_E + count_e
# print('Count:', count_res)

# x = "Еживику для ежат \
#      Принесли два ежа.\
#      Ежевику еле - еле\
#      Ежата возле ели съели."
#
#
# x =x.replace(',', '')
# x = x.replace('.', '')
# x = x.replace('-', '')
#
# l = x.split()
# print(l)
#
# count = len(l)
# print('Count: ', count)

# s = "Дана строка (символов, среди которых) есть одна открывающаяся"
# # y = s.replace('(', '')
# # y = s.replace(')', '')
# # y = s.replace(',', '')
#
# # z = s.index('(',3)
# #
# # print(z)
#
# index_1 = s.index('(')
# index_2 = s.index(')')
# print(index_2)
# print(index_1)
#
# print('Вывести слово в скобке:', s[index_1+1:index_2])

# s = "(У меня будет хорошая девушка, которая меня понимает и заботиться обо мне так и будет!)"
# index_1 = s.index('(')
# print(index_1)
#
# index_2 = s.index(')')
# print(index_2)
#
# print("Вывести на экран: ", s[index_1 + 1:index_2])

# s = 'Леша на полке клопа нашел'
# s = s.lower()
# print(s)
#
# s = s.replace(" ", '')
# print(s)
#
# a = reversed(s)
# print(a)

# x = b'A'
# print(x)
# c = bytes([65])
# print(c)
# z = b'\x41'
# print(z)

# x = bytes([73])
# print(x)
#
# z = b'\x45'
# print(z)
#
# c = bytes([2])
# print(c)

# c =bytes.fromhex('2Ef0 F1f2')
# print(c)
#
# z = bytes.fromhex('1fd ')
# print(z)

# a = b'abc'
# a.replace(b'a', b'f')
# print(a)
#
# a = b'1,2,3'.split(b',')
# print(a)
#
# b = b'1,2,3'.split(b',',maxsplit=1)
# print(b)
#
# c = b'1,2,3,'.split(b',')
# print(c)
#
# w = b'www.example.com'.lstrip(b'cmowz.')
# print(w)

# x = [1,2,3, 'txt']
# x.append(4)
# print(x)
#
# a = [1,2,3,'txt']
# a.insert([1], [90])
# print(a)
#
# a = [1,2,3,4]
# print(set(a))
# print(a)
# print(max(a))
#
# s = set()
# print(s)
#
#
# x = frozenset()
# print(x)
#
# a = set([1,2,3,4,'txt'])
# print(a)
# a.remove(3)
# a.remove(1)
# a.remove('txt')
# a.remove(2)
# a.add(1)
# a.add('txt')
# print(a)


# b = frozenset([1,2,3,4,5,6,7])
# print(b)
#
# b.remove([2])
# print(b)

# a = "sdfa fg rt ty" "df e"  'fg sdf' 'dg' 'cv' 'df'
# l = a.split()
# print(l)

# a = {'df', 'd', 'cvv'}
# print('d' in a)

# a = {1,2,3, 'txt'}
# b = {1,2,3,'txt'}
# print(a == b)

# backet = {'apple', 'orange', 'pear', 'cucumber'}
# print(backet)
# print('orange' in backet)
# print('pear' in backet)
# print('asbv' in backet)

# b = set('abracadabra')
# c = set('alacazam')
# print(b | c)

# b = set('adb')
# b.add('dsf')
# print(b)
# b.discard(d)
# print(b)

# s = 'Дан небольшой текст. Проверить количество уникальных символов в данном тексте.'
# unique_simbol = set(s)
# print(len(unique_simbol))
#
# x = 'На мели мы налима лениво ловили, меняли налима вы мне на линя!'
# x = x.lower()
# unique_simbol_1 = set(x)
# print(unique_simbol_1)
# print(len(unique_simbol_1))
#
# l1 = [1,2,3,4,5,6,7,8,9,10]
# l2 = [1,2,3,4,5,6,7,8,9,0,11,12,13,14]
#
# s1 = set(l1)
# s2 = set(l2)
#
# print(s1)
# print(s2)
#
# common_element = s1 & s2
# sorted_common_elem = sorted(common_element,)
# print('Общие элементы в порядке возрастания:' , sorted_common_elem)
#
# other_element = s1 ^ s2
# sorted_other_element = sorted(other_element, reverse=True)
# print('Разные элементы в порядке убывания:', sorted_other_element)

# s1 = {1,2}
# s2 = {3}
# s3 = {4,5}
# s4 = {3,2,6}
# s5 = {6}
# s6 = {7,8}
# s7 = {9,8}
#
# # s = s1 | s2 | s3 | s4 | s5 | s6 | s7
#
# s = s1.union(s2,s3,s4,s5,s6,s7)
# print(s)
# count = len(s)
# print('Для уникальных множестве:', count)
#
# max_element = max(s)
# min_element = min(s)
# print('Максимальный элемент равен:', max_element)
# print('Минимальный элемент равен:', min_element)


# my_dict = {}
# my_dict['Country'] = "Mexico"
# print(my_dict)

# my_dict = {'number': 23, 2: True, 'my_list': [1,2,3]}
# print(my_dict)
# print(my_dict.keys())
# print(my_dict.values())

# d = {1: 'one', 3: 'sdfasdf'}
#
# print(iter(d))
# print(list(iter(d)))
#
# print(d)

# d = {1: 'one', 2: [1,2,3], 3: 'fsdffsdf'}
# print(d.items())
# print(d.keys())
# print(d.values())

# d = {1: 'one', 2: [1,2,3], 3: 'text'}
# print(d.keys())
# d.update({4: 'new'})
# print(d)
# print(d.keys())
# print(d.values())
# dishes = {'eggs': 2, 'sausage': 3.14, 'bacon':21}
# dishes.update({'salad': 6})
# print(dishes)
# print(dishes.keys())
# print(dishes.values())
# print(len(dishes))
#
# del dishes['eggs']
# print(dishes)
# print(dishes.keys())
# print(dishes.values())

# dict = {0:10, 1: 20}
# # print(dict)
# # dict.update({2:30})
# # print(dict)
# dict[2] = 30
# print(dict)
#
# dict[1.3] = 40
#
# print(dict)

# a = {1:20, 2:20}
# b = {3:30, 4:40}
# c = {5:50, 6:60}
#
# a.update(b)
# a.update(c)
# print(a)

# dict = {'data': 100, 'data2': -54, 'data3': 247}
# values = dict.values()
# print(values)
#
# sum = sum(values)
# print(sum)

# stock = {'tesla': 400, 'apple': 55, 'aeroflot': 1}
# values = stock.values()
# print(values)
#
# sum_stock = sum(values)
# print('Сумма всех акций равна:', sum_stock)

# dict = {'a': 500, 'b': 5874, 'c':560, 'd': 400, 'e':5874, 'f': 20}
# values = dict.values()
# print(values)
# max_values = max(values)
# print(max_values)
# sort_dict = sorted(values, reverse=True)
# print(sort_dict)
# print('Наибольшее число равен:', sorted(sort_dict[0]))

# person = {'name': 'Kelly', 'age':25, 'salary': 80000, 'sity': 'New-York'}
# new_person = {'name': person.pop('name'), 'salary': person.pop('salary')}
# print(person)
# print(new_person)

# d = {'name': 'Kelly', 'age':25, 'salary': 80000, 'sity': 'New-York'}
# d['location'] = d.pop('sity')
# print(d)

# d = {'emp1':'{Name:' 'John', 'salary': 7500}}
# print(d)

# s = [1,2,3,4]
# d = iter(s)
# print(d)
# print(next(d))
# print(next(d))
# print(next(d))
# print(next(d))
# print(next(d))

# g = [1,2,3,4]
# x = iter(g)
# print(x)

# g = (1,2,3,4)
# x = iter(g)
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))

# def f():
#     return {'dsf', 123}
# def genf():
#     for i in {'sdaf', 2134}:
#         yield i
# s = genf()
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))

# a = 5
# print(id(a))
# print(type(a))
# print(a)
#
# b = 12
# print(id(b))
# print(type(b))
# print(b)
#
# c = 5.7
# print(id(c))
# print(type(c))
# print(c)
#
# a = 12
# print(id(a))
#
# a = 5.7
# print(id(a))
#
# a = b = c =125
# print(id(a))
# print(id(b))
# print(id(c))

# a = 5
# print('Type a:', type(a), ', id' , id(a))
#
# b = 12
# print('Type b:', type(b), ',id:' , id(b))
#
# c = 5.7
# print(type(c), id(c), 'ID c:', id(c) == id(a))

# a = 9
# b = 17
# c = 5
# print('Проверить a больше b:', 9, 17, a > b)
# print('Проверить а не равно разности б и с:', a, b-c, a != b - c)
# print('Проверить b равно сумме разности a и c:', b, a + c , b == a + c)
# print('Проверить c меньше или равно сумме a и b:', c, a + b, c <= a + b)
# print('Проверить a меньше b, но больше с:', a,b,c, a< b and a > c)
# print('Проверить b больше a или b больше с:',a,b,c, b > a or b > c)

# a = []
# print(type(a), id(a), bool)

# a = None
# # print(type(a), id(a))
# print('a is True:', a is True)
# print('a is True:', a is False)
# 
# b = bool
# print('b is True:', b is True)
# print('b is True:', b is False)
# 
# c = 2
# print('c is True:', c is True)
# print('c is True:', c is False)

# import math
#
# a = 100
# y1 = math.pow(((1 + a + a ** 2) / (2 * a + a ** 2) + 2 - (1 - a + a ** 2) / (2 * a - a ** 2)), -1) * (5 - 2 * a ** 2)
# print(y1)
#
# a = math.radians(90)
# b = math.radians(90)
# g = math.radians(90)
#
# y2 = 1 / 4 * (math.sin(a + b - g) + math.sin(b + g - a) + math.sin(g + a - b) - math.sin(a + b + g))
# print(y2)


# l = ['abc', 'xyz', 'aba', '1221']
# elem = l[0]
# print(elem, len(elem) > 2 and elem[0] ==elem[-1])
#
# elem = l[1]
# print(elem, len(elem) > 2 and elem[0] ==elem[-1])
#
# elem = l[2]
# print(elem, len(elem) > 2 and elem[0] ==elem[-1])
#
# elem = l[3]
# print(elem, len(elem) > 2 and elem[0] ==elem[-1])


# colors = ['red', 'green', 'white', 'black', 'pink', 'yellow']
# new_colors = [colors.pop(0), colors.pop(3), colors.pop(3)]
# print(new_colors)

# l1 = [-8, 1, 2, -2, 0]
# l2 = [1,1,0,0,2,-2,-2]
# l3 = [1,-1,0,-9,4,-5]
# l4 = [1,4,0,23,6,34]
#
# s1 = sorted(set(l1))
# s2 = sorted(set(l2))
# s3 = sorted(set(l3))
# s4 = sorted(set(l4))
#
# print(s1[1], s2[1], s3[1], s4[1])
#
# a = 'asdf'


# team1 = ['Alex', 'Robert', 'Player1', 'Player2', 'Player3']
# team2 = ['Petr', 'Antonio', 'Player1', 'Player2', 'Player3']
# team3 = ['John', 'Lucky', 'Player1', 'Player2', 'Player3']
#
# common_list = [team1, team2,team3]
# print(common_list[0][0])

# list = [0,1,2,3,4,5,6,7,8,9,10]
# print(sum(list))
#
# list5 = [0,1,2,3,4,5]
# print(sum(list5))

# n = 100
#
# l = range(n+1)
# sum_elem = sum(l)
# print('Сумма элементов равна:', sum_elem)


# psw = 'abcd12@S'
#
# cond1 = len(psw) >= 5
# # print(cond1, set(psw))
# cond2 = not psw.islower() and not psw.isupper()
# cond3 = len({"1",2,3,4,5,6,7,8,9,0} & set(psw)) > 0
# print(cond3, set(psw))
# cond4 = len({'@', "#", "%", "&"}  & set(psw)) > 0

# print('Пароль являетсяя достаточно сложным:', cond1 and cond2 and cond3 and cond4)

# text = 'In a distant, but not so unrealistic, future where mankind had abandoned earth because it has become covered with trash'
# print('Длина текста:' ,len(text))
# print('Текст в нижнем регистре:', text.lower())
# print('Текст в верхнем регистре:', text.upper())
# print('Текст после замены имени:', text.replace('distant', 'fuck'))
# print('Посчитать сколько раз было употреблено слово "earht":', text.count('earth'))

# byte_str = b'restart'
# print(byte_str)

# l = range(1,2)
# sum_elem = sum(l)
# print(sum_elem)

# s = "All the world's a stage, and all the"
# s = s.lower()
# print(s)
# str_set = set(s)
# print(len(str_set))
# print(min(str_set))
# print(max(str_set))

# a = {1,2,3,4,5}
# b = {4,5,6,7,8}
# print('Объядиняем а и б:', a.union(b))
# print('Пересечения а и б:', a & b)
# print('Sym difference:', a ^ b)

# math = ['Matvei', 'Evgenia', 'Michail', 'Maxim', 'Natalya']
# physics = ['Maxim', 'Matvei', 'Aleksandr']
#
# math1 = set(math)
# print(math1)
#
# physics1 = set(physics)
# print(physics1)
#
# all = math1.union(physics1)
#
# print('Объядиняем списки:', all)
# print('Призеры обеих олимпиад:', math1 & physics1)

# a = 5
# if a > 10:
#     print('Все хорошо, бро')
# else:
#     print('Не очень хорошо')

# my_money = 1000000000
# if my_money < 5000000:
#     print('Бля я ппс лузер')
# else:
#     print('Бля я ппс супер богатый')


# if m ==1:
#     print('Январь')
# elif m==2:
#     print('Февраль')
# elif m ==3:
#     print('Март')
# elif m ==4:
#     print('Апрель')
# elif m == 5:
#     print('Май')
# elif m == 6:
#     print('Июнь')
# elif m == 7:
#     print('Июль')
# elif m == 8:
#     print('Август')
# elif m == 9:
#     print('Сентябрь')
# elif m == 10:
#     print('Октябрь')
# elif m ==11:
#     print('Ноябрь')
# elif m ==12:
#     print('Декабрь')
# else:
#     print('Error')

# m = 1
# months = ['Январь', 'Февраль', 'Март',
#           'Апрель', 'Май', 'Июнь',
#           'Июль', 'Август', 'Сентябрь',
#           'Октябрь', 'Ноябрь', 'Декабрь']
# if 0 < m < 13:
#     print(months[m-1])
# else:
#     print('ERROR')

# F = 60
# C = (F -32) * 5/9
#
# print(C)
#
# C = 60
# F = C * 9/5 + 32
# print(F)

# a = 10
# b =34
# sum = a + b
# if sum in range(15,21):
#     print(20)
# else:
#     print(sum)

# a = 3
# b = 3
# c = 2
#
# if a == b == c:
#     print('равносторонний треугольник')
# else:
#     print('Неравносторонний')

# from math import sqrt
#
# a = 2
# b = 4
# c = 10
#
# d = b ** 2 - 4 * a * c
#
# if d >= 0:
#
#     print(x1,x2)
# else:
#     print('Корней нет')

# from math import sqrt, fabs
#
# a = 2
# b = 4
# c =10
#
# D = b ** 2 - 4 * a * c
# if D >= 0:
#     x1 = (-b + sqrt(D)) / (2 * a)
#     x2 = (-b -sqrt(D)) /  (2 * a)
#     print(x1,x2)
# elif D < 0:
#     x1 = -b / (2*a)
#     x2 = sqrt(fabs(D))/(2*a)
#     print(x1,x2)
# else:
#     print('ERROR')

# i =1
# while i < 6:
#     print(i)
#     i+=1

# a = 10
# while a < 17:
#     print(a)
#     a +=1

# i = 10
# while i > 7:
#     print(i)
#     i +=-1

# from math import pi
# from math import sin
# from math import cos
#
# e = 2.7
# x = 0
# y = (e**(sin(x))*cos(x))
#
# while y < pi:
#     print(round(y,2))
#     y+=0.1

# N = 4
# sum = 0
# i =2
# while i <= N:
#     sum += i
#     i +=2
# print(sum)

# list = [1452, 11.23, 1+2j, True, 'Hello, Python', (0, -1), [5,12], {'class': 'v', 'section': 'A'}]
# i = 0
# while i < len(list):
#     elem = list[i]
#     print(elem,type(elem))
#     i += 1

list = [12,15,32,42,55,75,122,132,150, 180,200]
i = 0
while i<len(list):
    elem = list[i]
    if elem%5==0 and elem <=150:
        print(elem)
    i +=1