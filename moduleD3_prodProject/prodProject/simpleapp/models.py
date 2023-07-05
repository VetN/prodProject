from django.db import models
from django.core.validators import MinValueValidator

class Product(models.Model):
    name = models.CharField(max_length=200,unique=True) # unique=True - названия не должны повторяться
    description = models.TextField()
    quantity = models.IntegerField(validators=[MinValueValidator(0, 'Quantity should be >= 0')])# количество товара на складе
    # поле категории будет ссылаться на модель категории
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE, related_name='products')
    # все продукты в категории будут доступны через поле products
    price = models.FloatField(validators=[MinValueValidator(0.0)],)
    #price = models.FloatField(default=0.0)
    def __str__(self):
        return f'{self.name.title()}: {self.description[:20]}'
        #return f'{self.name} {self.quantity}'
 
 
#  создаём категорию, к которой будет привязываться товар
class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
 
    def __str__(self):
        return f'{self.name.title()}'
        #return f'{self.name}'