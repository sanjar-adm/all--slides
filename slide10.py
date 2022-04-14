# # 1
# lang1 = 'ruby'
# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# for i in languages:
#     if lang1 == i:
#         print('this languages is in list')
# # 2
# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# i = 0
# while i < len(languages):
#     if languages[i] == 'php':
#         break
#     print(languages[i])
#     i += 1
#
# # 3
# a = 7
# for i in range(5):
#     a *= a
#     print(a)
# # 4
# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# c = 0
# for i in languages:
#     print(c, i)
#     c += 1
# # 5
# a = 11
# c = 1
# for i in range(a):
#     print(i)
#
# for i in range(10, 0, -1):
#     print(i)
#
# # v2
# print(list(range(10)) + list(range(10,-1,-1)))
# # 6
# names = ('Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан',)
# for i in range(len(names)):
#     if i % 2 == 0:
#         print(names[i])
# # 7
# names = ('Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан',)
# for i in range(0,len(names),2):
#     print(names[i])
# # 8
# x = 123
# if 3 == len(str(x)):
#     print('Это число трёхзначное?')
# x1 = 124
# if x1 > 0 and  x % 2 == 0:
#     print('Это число положительное и чётное')
# x2 = 2323
# if x2 % 31 == 0:
#     print('Это число делится на 31 без остатка?')
# x3 = 3423423423
# if x3 > 100 and x3 % 17 == 0 or x3> 150 and x3 ==13**2:
#     print(x3)
# 9
a = 200
for i in range(-100 ,100):
    print(i)
    if i % 13:
        print(i**2)
    if i / 2 == 0:
        print('не четное')

