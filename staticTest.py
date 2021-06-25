# class StaticTest:
#     x = 1
# t1 = StaticTest()
# print(f'Via instance: {t1.x}')
# print(f'Via class:{StaticTest.x}')
# t1.x = 2
# print(f'Via instance:{t1.x}')
# print(f'Via class:{StaticTest.x}')
#
#
# class Date:
#     def __init__(self,month,day,year):
#         self.month = month
#         self.day = day
#         self.year =year
#
#     def display(self):
#         return f"{self.month}-{self.day}-{self.year}"
#     @classmethod
#     def millenium_c(cls,month,day):
#         return cls(month,day,2000)
#
#     @staticmethod
#     def millenium_s(month,day):
#         return Date(month,day,2000)
#
#
# class User:
#     def __init__(self,name,email):
#         self.name = name
#         self.email = email
#     def get_info(self):
#         print(f'{self.name} - {self.email}')
#
# user = User('Admin', 'info@test.com')
# user.get_info()
#
#
# class Shape():
#     def __init__(self):
#         print('Shape created')
#
#     def draw(self):
#         print('Drawing a shape')
#
#     def area(self):
#         print('Calc area')
#     def perimeter(self):
#         print('Calc perimeter')
#
# shape = Shape()
# Shape created
#
# class Person:  #parent
#     def can_breathe(self):
#         print('Я могу дышать')
#
#     def can_walk(self):
#         print('Я могу ходить')
#
# class Doctor(Person): #subclass
#
#     def can_cure(self):
#         print('Я могу лечить')
#
# class Ortoped(Doctor):
#     pass
#
#
# class Architect(Person): #subclass
#     def can_build(self):
#         print('Я могу строить что угодно')
#
#
#
# d = Doctor()
#
# e = Ortoped()
# e.can_cure()
# e.can_walk()
# e.can_breathe()
#
# class Rectangle:
#
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#
#     def get_rect_area(self):
#         return self.a * self.b
#
# class Square:
#     def __init__(self,a):
#         self.a = a
#     def get_sq_area(self):
#         return self.a**2
#
# class Doctor:
#     def can_cure(self):
#         print('Я доктор, я умею лечить')
#
# class Builder:
#     def can_build(self):
#         print('Я строитель, я могу строить')
#
# class Person(Doctor, Builder):
#     pass
#
# s = Person()
# s.can_cure()
# s.can_build()
#
# class Rectangle:
#     __slots__ = 'width', 'height',
#
#     def __init__(self, a,b):
#         self.width = a
#         self.height = b
#
# class Vehicle:
#     def __init__(self, position):
#         self.position = position
#     def travel(self, destination):
#         route = calculate_route(source=self.position, to = destination)
#         self.move_along(route)
#     def calculate_route(self, source, to):
#         return 0
#     def move_along(self, route):
#         print('moving')
#
# class Car(Vehicle):
#     pass
#
# class Airplane(Vehicle):
#     pass
#
# class RadioMixin:
#     def __init__(self):
#         self.radio = Radio()
#     def turn_on(self, station):
#         self.radio.set_station(station)
#         self.radio.play()
#
# class Radio:
#     def set_station(self, station):
#         self.station = station
#     def play(self):
#         print(f'Playing {self.station}')
#
# class Car(Vehicle, RadioMixin):
#     def __init__(self):
#         Vehicle.__init__(self, (10,20))
#         RadioMixin.__init__(self)
#
# car = Car()
# car.turn_on('Moscow FM')
#
# from abc import ABC
# from abc import abstractmethod
#
# class Shape(ABC):
#     def __init__(self):
#         super().__init__()
#
#     @abstractmethod
#     def draw(self):
#         pass
#
#     @abstractmethod
#     def area(self):
#         pass
#     @abstractmethod
#     def perimeter(self):
#         pass
#
# class Point():
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f'Point x = {self.x}, y = {self.y}'
#
# p = Point(3,4)
# print(p)
#
# class Road():
#     def __init__(self, length):
#         self.length = length
#
#     def __len__(self):
#         return self.length
#
#     def __str__(self):
#         return f'A road of lenght:{self.length}'
#     def __del__(self):
#         print(f'The road has been destroyed')
# r = Road(100)
# print(len(r))
# print(r)
#
# class BankAccount:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
# b = BankAccount
# b.name
#
# class Name:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name.lower().capitalize()
#         self.first_name = first_name.title()
#         self.last_name = last_name.title()
#         self.full_name = self.first_name + " " + self.last_name
#         self.initials = self.first_name[0] + " " + self.last_name[0]
# n = Name('SDfdesaASDFe', "True")
# print(n.first_name)
# print(n.last_name)
# print(n.full_name)
# print(n.initials)
#
#
# class Calculator:
#     def add(self, a,b):
#         return a+b
#     def subtract(self, a,b):
#         return a - b
#     def multiplay(self, a,b):
#         return a*b
#     def divide(self, a, b):
#         return a/b
#
# c = Calculator()
# c.add(1,2)
#
# class Employee:
#     def __init__(self, first_name, last_name, salary):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.salary = salary
#
#     @classmethod
#     def from_string(cls, str_to_parse):
#         data = str_to_parse.split('-')
#         return cls(data[0], data[1], int(data[2]))
#
#         first_name, last_name, salary = str_to_parse.split('-')
#         return cls(first_name, last_name, int(salary))
# emp = Employee.from_string('John-Smith-55000')
# print(emp.first_name)
# print(emp.last_name)
# print(emp.salary)
#
# class Pizza:
#     order = 0
#
#     def __init__(self, ingredients):
#         self.ingredients = ingredients
#         Pizza.order += 1
#         self.order_number = Pizza.order
#
#     @classmethod
#     def hawaiian(cls):
#         return cls(['ham', 'pineapple'])
#
#     @classmethod
#     def meat_festival(cls):
#         return cls(['beef', 'meatball', 'bacon'])
#
#     @classmethod
#     def garden_feast(cls):
#         return cls(['spinach', 'olives', 'mushroom'])
#
# p1 = Pizza(['ham', 'bacon'])
# p2 = Pizza.garden_feast()
# p3 = Pizza.hawaiian()
# p4 = Pizza(['beef', 'olives'])
#
# print(Pizza.order)
# print(p1.order_number)
# print(p2.order_number)
# print(p3.order_number)
# print(p4.order_number)
#
# import math
# class Circle:
#
#     def __init__(self, r=0):
#         self.r =r
#
#     def get_area(self):
#         return math.pi * self.r **2
#
#     def get_perimeter(self):
#         return 2*math.pi*self.r
# c = Circle(4.44)
# c.get_perimeter()
#
# c.get_area()
#
# prices = {'Strawberries': 1.5, 'Banana': 0.5, 'Mango': 2.5,
#           'Blueberries': 1, 'Raspberries': 1, "Apple": 1.75,
#           'Pineapple': 3.5}
# class Beverage:
#     def __init__(self, ingredients):
#         self.ingredients = ingredients
#         self.cost = sum([prices[fruit] for fruit in self.ingredients])
#         self.price = self.cost * 2.5
#
#     def get_cost(self):
#         return f'${self.cost:.2f}'
#
#     def get_price(self):
#         return f'${self.price:.2f}'
#
#     def get_name(self):
#         lst = sorted([i.replace('ies', 'y') for i in self.ingredients])
#         return f'{" ".join(lst)} {"Fusion" if len(lst) > 1 else "Smoothie"}'
#
# b1 = Beverage(["Raspberries", "Strawberries", "Blueberries"])
# print(b1.ingredients)
# print(b1.get_cost())
# print(b1.get_price())
# print(b1.get_name())
#
#
#
# board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
#
#
# def print_state(state):
#     for i, c in enumerate(state):
#         if (i + 1) % 3 == 0:
#             print(f'{c}')
#         else:
#             print(f'{c}|', end='')
#
# print_state(board)
#
#
# from datetime import datetime
# from datetime import date
# from datetime import time
# from datetime import timedelta
#
# d1 = date(2019, 3, 12)
# print(d1)
# print(d1.year)
# print(d1.month)
# print(d1.day)
#
#
# t1 = time(23,10,59)
# print(t1)
# print(t1.hour)
# print(t1.minute)
# print(t1.second)
#
# print(date.today())
# print(date.max)
# print(date.min)
# print(time.max)
# print(time.min)
#
# dt = datetime(2019,3,12,15,17,34,34)
# print(dt.date().year)
# print(dt.time().hour)
#
# import locale
# locale.setlocale(locale.LC_ALL, "")
# 'Russian_Russia.1251'
# now = datetime.now()
# print(now.strftime('%Y-%m-%d (%a)'))
# print(now.strftime('%Y %B %d число (%A)'))
#
# class Character:
#     def __init__(self):
#         self.race = 'Elif'
#
#
# c = Character()
# c.race
#
# lst = [1,2,3]
# repr(lst)
# print(lst)
# eval(repr(lst)) == lst
# class Character():
#     def __init__(self, race, damage = 80):
#         self.race = race
#         self.damage = damage
#     def __repr__(self):
#         return f"Character('{self.race}', {self.damage})"
#     def __str__(self):
#         return f'{self.race} with damage = {self.damage}'
#
# c = Character('Elif')
# print(c)
# d = eval(repr(c))
# print(d)
#
# list1 = [1,2,3,[4,5,6]]
# copied_list = list1.copy()
# copied_list[3].append(7)
# # print(list1)
# # print(copied_list)
# # list1.append(8)
# # print(list1)
# # print(copied_list)
# # copied_list.append(10)
# print(list1)
# print(copied_list)
#
# list1 = [1,2,3,[4,5,6]]
# copied_list = list1.copy()
# import copy
# shallow_copy = copy.copy(list1)
# shallow_copy[3].append(7)
# print(list1)
# print(shallow_copy)
#
# deep_copy = copy.deepcopy(list1)
# deep_copy[3].append(9)
# print(list1)
# print(deep_copy)
#
# numbers = [1,2,3,4,5]
# new_numbers = numbers
# new_numbers[0] = 9
# print('Numbers list:' , numbers)
# print('ID of numbers:', id(numbers))
#
# print('New numbers:', new_numbers)
# print('ID of new numbers:' , id(new_numbers))
#
# import copy
#
# old_list = [[1,2,3], [4,5,6],[7,8,9],[10,11,12]]
# new_list = copy.copy(old_list)
# new_list[3] = ['a','b','c']
# print("Old list:", old_list)
# print("New list:", new_list)
#
# from enum import Enum
#
# class TrafficLight(Enum):
#     RED = 1
#     YELLOW = 2
#     GREEN = 3
# print(TrafficLight.GREEN)
# for c in TrafficLight:
#     print(c)
#
# import random
#
#
# def randoms(min, max, n):
#     return [random.randint(min, max) for _ in range(n)]
#
#
# for r in randoms(10, 30, 5):
#     print(r)
#
# def randoms(min, max, n):
#     for i in range(n):
#         yield random.randint(min,max)
#
# for r in randoms(10,30,5):
#     print(r)
#
# rand_sequence = randoms(1,10,10)
# print(rand_sequence )
#
# for r in rand_sequence:
#     print(r)
#
# for r in rand_sequence:
#     print(r)
# seq = list(randoms(1,20,5))
# print(seq)
# print(seq)
#
# import itertools
# rand_sequence = randoms(1,10,10)
# five_taken = list(itertools.islice(rand_sequence,5))
# print(five_taken)
#
# my_list = [1,2,3,4]
# squares = [x**2 for x in my_list]
# print(squares)
#
# iterable = [1,2,3]
#
# iterator = iter(iterable) #будет вызван метод __iter__()
# print(type(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
#
# import itertools as it
# even_numbers = [x for x in range(10) if x % 2 ==0]
# print(even_numbers)
#
# even_numbers = it.count(0,2)
# print(even_numbers)
#
#
# print(list(next(even_numbers) for _ in range(5)))
#
# print(list(zip(it.count(), ['a', 'b', 'c'])))
#
# print(list(it.dropwhile(lambda x: x<3, [1,2,3,4,5])))
#
# print(list(it.takewhile(lambda x: x<3, [1,2,3,4,5])))
#
# print(list(it.filterfalse(lambda x: x%2 == 0, range(10))))
#
# names = ['Carlsen', 'Caruana', 'Mamedyarov', 'Ding', 'Giri']
# ratings = [2842,2822,2801,2797,2780]
# for name, rating in zip(names, ratings):
#     print(f'{name}: {rating}')
#
# print(list(zip(names, ratings)))
#
# # pin = [7,5,2,8,3,4,9]
# # print(list(it.permutations(pin)))
#
# ranks = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
# suits = ['H', 'D', 'C', 'S']
# lst = list(it.product(ranks, suits))
# print(lst)
#
# import requests
# response = requests.get('https://www.ykt.ru/')
# print(response)
# print(type(response))
#
# print(response.status_code)
#
# from requests import HTTPError
#
# for url in ["https://www.ykt.ru", "https://vk.com"]:
#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#     except HTTPError as http_err:
#         print(f'Error:{http_err}')
#     except Exception as err:
#         print(f'Unknown erro: {err}')
#     else:
#         print('Connected Successfully')
#
# response = requests.get('https://ykr.ru')
# print(response.content)
#
#
# from getpass import getpass
# auth_pesponse = requests.get("https://api.github.com/user, auth = ('EngineerSpock", getpass())
#

# class Character:
#     def __init__(self, armor: int, power: int, health: int):
#         self.armor = armor
#         self.power = power
#         self.health = health
#
#     def hit(self, damage: int):
#         self.health -= damage
#
#     def is_alive(self):
#         return self.health > 0
#
# c1 = Character(1,2,3)
#
# c1.hit(20)
# amount: int
# amount = None
#
# price: Optional[int]
# price =10
# price = None
# price = "abcdef"
#
# attack: Any = 1
# attack= "hi"



# class Question:
#     def __init__(self, text, is_true, explanation):
#         self.text = text
#         self.is_true = is_true
#         self.explanation = explanation
#
# from dataclasses import dataclass
# @dataclass
# class Question:
#     text: str
#     is_true: bool
#     explanation: int
#
# q = Question("test", True, False)
# print(q.text)
# print(q.is_true)
# print(q.explanation)

# walrus = True
# print(walrus)

# print(walrus:=False)
# print(type(walrus))

# for i in range(rows := int(input('Enter the number of rows'))):
#     print('*' * (i + 1))
# print(f'Number of rows:{rows}')

# def avg(a,b,c):
#     return (a+b+c) / 3
# print(avg(5,6,7))
# print(avg(a = 4, b = 3, c = 1))

# class Dog:
#     def __init__(self):
#         self.paws = 4
#         self.health = 100
#         self.sound = 'woof - woof'
#
#     def bark(self):
#         print(self.sound)
#
# class SuperDog(Dog):
#     def __init__(self):
#         super().__init__()
#         self.health = 200
#         self.sound = 'super-woof'
#
# dog = SuperDog()
# print(dog.health)
# dog.bark()

def parse_roman(roman):
    romans = dict(I=1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000)
    result = 0
    for i, c in enumerate(roman):
        if i + 1 < len(roman) and romans[roman[1]] < romans[roman[i +1]]:
            result -=romans[roman[i]]
        else:
            result += romans[roman[i]]
    return result

def add(x:str, y=str, to_arabic: bool) -> Union[str, int]:
    a = parse_roman(x)
    b = parse_roman(y)

    c = a + b

    return c if to_arabic else convert_to_roman(c)

result1 = add('I', 'II', False)
