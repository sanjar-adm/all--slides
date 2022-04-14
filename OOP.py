class Laptops:
    my_dict = {}
    def __init__(self,name,CPU,RAM,graphics_card,HDD,mainboard,display_size):
            self.my_dict['Модель'] = name
            self.my_dict['Процессор'] = CPU
            self.my_dict['Оперативка'] = RAM
            self.my_dict['Видео карта'] = graphics_card
            self.my_dict['Жесткий диск'] = HDD
            self.my_dict['Материнка'] = mainboard
            self.my_dict['Размер экрана'] = display_size

    def return_dict(self):
        return self.my_dict

Acer = Laptops('Asus','Intel Core i5',16,'GeForce GTX774',128,'Gigabit',18)
Asus = Laptops('Asus','Intel Core i7',8,'GeForce GTX771',500,'Gigabit',28)
Lenovo = Laptops('Asus','Intel Core i8',4,'GeForce GTX772',256,'Gigabit',34)
HP = Laptops('Asus','Intel Core i9',8,'GeForce GTX773','1TB','Gigabit',24)

# das = Acer.return_dict()
# for i, j in das.items():
#     print(i, j)
print(Acer.return_dict())
print(Asus.return_dict())
print(HP.return_dict())
