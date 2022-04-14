# # 1
# a = open('/Users/sanjar/Desktop/directories.txt','r')
# print(a.read())
# a.close()
#
# # 2
# a = input('Введите логин :')
# b = input('Введите пароль :')
# a1 = open('test.txt', 'w')
# a1.write(a)
# a1.write(b)
# a1.close()

# 3
# a1 = open('test1.txt', 'w')
# a1.write('Shawn Mendes')
# a1 = open('test1.txt','r')
# if 'w' in a1.read():
#     print('В тексте есть w')
# else:
#     print('в тексте нет w')
# a1.close()

# 4
# a2 = open('python.txt','w')
# c = '''Python is a widely used high-level programming language for general-purpose
#
# programming, created by Guido van Rossum and first released in 1991. An interpreted
#
# language, Python has a design philosophy that emphasizes code readability (notably
#
# using whitespace indentation to delimit code blocks rather than curly brackets or
#
# keywords), and a syntax that allows programmers to express concepts in fewer lines of
#
# code than might be used in languages such as C++ or Java.'''
# a2.write(c)
# a2 = open('python.txt','r')
# t_words = []
# for i in a2.read().split():
#     if 't' in i or 'T' in i:
#         t_words.append(i)
# a2.close()
# print(t_words)

# 5
a2 = open('database.txt', 'w' )
a2.write('sanadm 123456')

a = input("Ввведите Логин :")
b = input("Введите пароль :")
a1 = "sanadm"
b1 = 123456
if a == a1 and b == b1:
    print("Welcome nigga!")
else:
    print("Вы ввели не правильно Гудбай!")

