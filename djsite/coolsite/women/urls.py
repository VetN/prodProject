from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
       # прописав тут name теперь можно работать именно
    # c везде name и если поменяется маршрут ' ' то ничего менять не придется
    path('caba/<slug:catid>/', categories),
    path('cabam/<slug:cat>/', categories_1),
    re_path(r'archive/(?P<year>[0-9]{4})/', archive),
]