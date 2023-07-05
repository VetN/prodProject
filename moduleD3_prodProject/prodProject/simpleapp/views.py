from django.shortcuts import render
from datetime import datetime
from django.views.generic import ListView, DetailView # импортируем класс(будет выводить список объектов из БД) DetailView- отвечает за детали(за 1 продукт)
#from django.views.generic import  DetailView 
from .models import Product
#from django.views import View # импортируем простую вьюшку
#from django.core.paginator import Paginator # импортируем класс, позволяющий удобно осуществлять постраничный вывод

# вариант с пагинацией, а не ListView

class ProductsList(ListView):
#class Products(View):
    model = Product  # указываем модель, объекты которой мы будем выводить
    template_name = 'flatpages/products.html'  # указываем имя шаблона, в котором будет лежать HTML, в нём будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'products'  # это имя списка, в котором будут лежать все объекты, его надо указать, чтобы обратиться к самому списку объектов через HTML-шаблон
    queryset = Product.objects.order_by('-id') # выводит список с конца

   # если пишем без джененриков(listView) то метод надо прописывать самим
    #def get(self, request):
       # products = Product.objects.order_by('-price')
       # p = Paginator(products, 1) # создаём объект класса пагинатор, передаём ему список наших товаров и их количество для одной страницы
       # products = p.get_page(request.GET.get('page', 1)) # берём номер страницы из get-запроса. Если ничего не передали, будем показывать первую страницу.
        # теперь вместо всех объектов в списке товаров хранится только нужная нам страница с товарами
        
       # data = {
            #'products': products,
       # }
       # return render(request, 'flatpages/products.html', data)
    
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        return context

class ProductDetail(DetailView):
    model = Product
    template_name = 'flatpages/product.html' 
    context_object_name = 'product'
