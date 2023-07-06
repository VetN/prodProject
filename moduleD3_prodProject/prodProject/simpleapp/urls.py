from django.urls import path, re_path
#from django.views import View
from .views import ProductsList, ProductDetail
#from .views import  ProductDetail, View
 
 
urlpatterns = [
   
    path('', ProductsList.as_view()),# т.к.это класс, то надо представить этот класс в виде view. Для этого вызываем метод as_view
    #path('products', ProductsList.as_view()),
    path('product/<int:pk>', ProductDetail.as_view(), name='product'),
    re_path(r'^products', ProductsList.as_view(), name = 'products') # маршрут позвол по-разному писать адрес при вызове
]
    # если прописываем просто через View


#urlpatterns = [
   # path('products', View.as_view()),
   # path('', View.as_view()),
   # path('/product/<int:pk>', ProductDetail.as_view(), name='product'),
#]