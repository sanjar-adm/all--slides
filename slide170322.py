# 1
menu = {'lagman': 120,
        'plov': '120',
        'borsh': 100}
drinks1 =['Coca-Cola', 'Sprite', 'Fanta']
menu['drinks'] = drinks1
print(menu)
# 2
slovar = {}
for i in range(3):
    name = input('имя')
    password = input('пароль')
    slovar[name] = password
# 3
dict1 = {
    'Sanzhar' : 'IT - Шник',
    'Avtandil' : 'Programmer',
    'Naraiym ' : 'Финансист',
    'Vin Disel' : 'Таксист'
}
for k, v in dict1.items():
    print('Здравствуйте', k  ,'Прекрасная профессия',v)

# 4
menu = {'lagman': 120,
        'plov': '120',
        'borsh': 100}
menu['besh_barmak'] = 130
print(menu)
menu['besh_barmak'] = 135
print(menu)
menu.pop('borsh')
print(menu)

# 5
south_american_countries = ['Argentina', 'Bolivia', 'Brazil', 'Chile',
                            'Colombia', 'Ecuador', 'Guyana', 'Paraguay',
                            'Peru', 'Suriname', 'Suriname', 'Uruguay', 'Venezuela']
new_dict = {}

for i in range(len(south_american_countries)):
    if south_american_countries[i] not in new_dict.values():
        new_dict[i] = south_american_countries[i]

print(new_dict)


# print({k: v in enumerate(set(south_american_countries))})
