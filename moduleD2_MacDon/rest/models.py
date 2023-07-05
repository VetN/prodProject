from django.db import models
from datetime import datetime  # позволяет получить текущее время
        # Представляем сущности в виде классов,
        # а объекты этих сущностей(строки) - в виде экземпляров этих классов


class Staff(models.Model):
            # создаем список кортежей, чтобы в поле position
            # вписывались только определ значения
    director = 'DI'
    admin = 'AD'
    cook = 'CO'
    cashier = 'CA'
    cleaner = 'CL'

    POSITIONS = [
        (director, 'Директор'),
        (admin, 'Администратор'),
        (cook, 'Повар'),
        (cashier, 'Кассир'),
        (cleaner, 'Уборщик')
    ]

    full_name = models.CharField(max_lenght = 255)
    position = models.CharField(max_lenght = 2, choices = POSITIONS, default = cashier )
    labor_contract = models.IntegerField()


    

class Product(models.Model):
    name = models.CharField(max_length = 255)
    price = models.FloatField(default = 0.0)
    composition = models.TextField(default = "Состав не указан")



class Order(models.Model): # наследуемся от класса Model
            # order_id - вводится автоматически, его заносить сюда не надо
            # auto_now_add = True- автом устанавл время и дату
    time_in = models.DateTimeField(auto_now_add = True)   

            # изначально время выдачи заказа неизвестно 
            # устан позже поэтому null = True
    time_out = models.DateTimeField(null = True)

    cost = models.FloatField(default = 0.0)

            # заказ с собой-true, на месте - false
    take_away = models.BooleanField(default = False)

            # заказ выполнен
    complete = models.BooleanField(default = False)

            # тип связи один ко многим сотрудник-заказ
    staff = models.ForeignKey(Staff, on_delete = models.CASCADE)
    
            #  поле модели products, реализует связь с моделью
            # Product через промежуточн таблицу ProductOrder
    products = models.ManyToManyField(Product, through = 'ProductOrder')


   

class ProductOrder(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    order = models.ForeignKey(Order, on_delete = models.CASCADE)
    _amount = models.IntegerField(default = 1, db_column = 'amount')



