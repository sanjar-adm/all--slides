# # 1
# def first_func():
#     print('Я главная функция!')
#     def second_func():
#         print('Я вложенная функция!')
#     return second_func()
# first_func()
#
# # 2
# def dict_fuct():
#     my_dict = {
#         'a': 1,
#         'b': 2,
#         'c': 3,
#         'v': 4
#     }
#     return tuple(my_dict.keys()),tuple(my_dict.values())
# print(dict_fuct())
#
# # 3
#
# def is_simple_number():
#     num = int(input('Введите число :'))
#     for i in range(2,num):
#         if num % i == 0:
#             return False
#     return True
# print(is_simple_number())

# # 4
# from random import randint
#
#
# def dell_duplicate(f):
#     def wrapper():
#         result = f()
#         return list(set(result))
#
#     return wrapper
#
#
# @dell_duplicate
# def random_numbers():
#     return [randint(10, 50) for _ in range(100)]
#
#
# print(random_numbers())

# 5
def question_l_p():

