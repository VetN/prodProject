from datetime import datetime
from django.shortcuts import render

# Create your views here.
def get_last_name(self):
        full_name = self.full_name
        f_n = full_name.split()
        return f_n[0];

def finish_order(self):
    self.time_out = datetime.now() # время now является завершен
    self.complete = True
    self.save()

def get_duration(self):
    if self.complete:
                # если заказ готов, то время ожидания
        return(self.time_out - self.time_in).total_seconds()
    else:
                # если не готов, то текущее время выполнения
        return(datetime.now() - self.time_in).total_seconds()

@property
def amount(self):
    return self.amount
    
@amount.setter
def amount(self, value):
    self._amount = int(value) if value >= 0 else 0
    self.save()
    
def product_sum(self):
        product_price = self.product.price  # стоимость продукта от кол-ва
        return product_price * self.amount  # кол-во текущего объекта
 