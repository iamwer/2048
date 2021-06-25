# import pdb
# x =1
# y=2
# pdb.set_trace()
# z = 3
# x+=1
# pdb.set_trace()
# print('finish')

# a = [i ** 2 for i in range(1, 6)]
# print(a)

# b = (x ** 2 for x in range(1, 6))
# print(b)

# выражения - Генераторы

# s = [1,2,3]
# d = iter(s)
# print(next(d))
# print(next(d))
# print(next(d))
# print(next(d))

# c = (i**2 for i in range(1,5))
# # print(c)
# # print(c)
# # print(c)
# # print(c)
# # print(c)
# # print(c)
# # print(c)
# # print(c)
#
# # print(next(c))
# # print(next(c))
# # print(next(c))
# # print(next(c))
# # print(next(c))
#
# for i in c:
#     print(i)
#
# for i in c:
#     print(i)

# c = list(range(100000000000000000000))
# print(c)

# c = [i for i in range(10000000000000000)]
# print(c)

# c = (i for i in range(10000000000))
# for i in c:
#     print(i)

# import json
# from random import randint
#
# str_json = """
# {
# "response": {
#     "count": 5946179,
#     "items": [{
#         "first_name": "Mikhail",
#         "id": 312023319,
#         "last_name": "Leschenko",
#         "can_access_closed": true
#
#     }, {
#         "first_name": "Irina",
#         "id": 654876916,
#         "last_name": "Smirnova",
#         "can_access_closed": true
# }]
# }
# }"""
# # print(type(str_json))
#
# data = json.loads(str_json)
# # print(type(data))
# for item in data['response']['items']:
#     del item['id']
#     item['likes'] = randint(100, 200)
# print(data['response']['items'])
# new_json = json.dumps(data)
# print(new_json)


# class MyClass:
#      def __init__(self,x,y):
#          self.x = x
#          self.y = y
# instance1 = MyClass(1,2)
# print(instance1)

# from dataclasses import dataclass, field
#
#
# @dataclass(order=True)
# class MyClass:
#     x: int
#     y: int
#     z: int = field(repr=False, default=3)
#
#     def __post_init__(self):
#         self.generated_attr = self.x +self.y + self.z
#
#
# instance1 = MyClass(1, 2)
# instance2 = MyClass(3, 4)
# print(sorted(instance1,instance2))

# def f():
#
#     return [34,23,12]
#
# def genf():
#     s = 7
#     for i in [3,2,3]:
#         yield i
#         print(s)
#         s = s*10+7
# g = genf()
# print(next(g))
# print(next(g))
# print(next(g))

a = [1,2,3,4,5,6,7,8,9]
a.append(10)
print(a)

x = [1,2,3,4,5,6,7,8,9,10]
print(x[2::2])

c = [1,2,3,4,5,6,7,8,9]
c.append('Hello')
print(c)

z = [1,2,3,4,5,6,7,8,9]
print(z[2:8:1])