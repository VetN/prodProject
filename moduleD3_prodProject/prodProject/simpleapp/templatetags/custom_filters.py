from django import template
 
register = template.Library() # если мы не зарегестрируем наши фильтры, то django никогда не узнает где именно их искать и фильтры потеряются

@register.filter(name='multiply') # регистрируем наш фильтр под именем multiply, чтоб django понимал, что это именно фильтр, а не простая функция
def multiply(value, arg): # первый аргумент здесь — это то значение, к которому надо применить фильтр, второй аргумент — это аргумент фильтра, т.е. примерно следующее будет в шаблоне value|multiply:arg
    return str(value) * arg # возвращаемое функцией значение — это то значение, которое подставится к нам в шаблон

# напишем фильтр, чтобы можно было умножить только строку на число
@register.filter(name='multiply_1')  
def multiply_1(value, arg):
    if isinstance(value, str) and isinstance(arg, int): # проверяем, что value — это точно строка, а arg — точно число
        return str(value) * arg
    else:
        raise ValueError(f'Нельзя умножить {type(value)} на {type(arg)}') # выводим ошибку