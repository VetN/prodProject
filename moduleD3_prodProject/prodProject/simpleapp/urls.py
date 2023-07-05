from django.urls import path
#from django.views import View
from .views import ProductsList, ProductDetail
#from .views import  ProductDetail, View
 
 
urlpatterns = [
   
    path('', ProductsList.as_view()),# т.к.это класс, то надо представить этот класс в виде view. Для этого вызываем метод as_view
    path('products', ProductsList.as_view()),
    path('product/<int:pk>', ProductDetail.as_view()),
]
    # если прописываем просто через View


#urlpatterns = [
   # path('products', View.as_view()),
   # path('', View.as_view()),
   # path('/product/<int:pk>', ProductDetail.as_view(), name='product'),
#]