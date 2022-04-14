# Напишите код где есть TypeError,IndexError,NameError
age = int(input('Введите возраст :'))
long_life = input('Сколько хотите прожить :')
ostat = long_life - age

# 2
age[214343256]

3
long_life = input('Сколько хотите прожить :')
long_life[4534645676]
print(er)

2 Задание
try:
    at = 10
    iin = 15
    wo = 20

    for e in range(-at, at):
        print(wo / e)
        if at > '5':
            print('at > 5')
except TypeError:
    print('Ошибка типов')


3
try:
    lst = []
    for i in range(10):
        lst.append(i)
    a = list(reversed(lst))
    sls_obj = slice('0','8')
    print(а[sls_obj])
except NameError:
    print('Ошибка Имени')

# 4
try:
    a = (0)
    b = (1)
    numbers = []
    while b > a:
        numbers += b
        b += 1
except TypeError:
    print("ошибка Типа")
