from django.shortcuts import render

# Create your views here.
cashier1 = Staff.objects.create(full_name = "Иванов Иван Иванович", position = Staff.cashier, labor_contract = 1754)
cashier2 = Staff.objects.create(full_name = "Петров Петр Петрович",
                                position = Staff.cashier, 
                                labor_contract = 4355)
direct = Staff.objects.create(full_name = "Максимов Максим Максимович",
                                position = Staff.director, 
                                labor_contract = 1254)
fries_stand = Product(name = "Картофель фри (станд.)", price = 93.0)
fries_stand.save()

fries_big = Product.objects.create(name = "Картофель фри (бол.)", price = 106.0)# Create your models here.
person = Staff.objects.get()
print(person)

class AbstractBaseUser(models.Model):
    password = models.CharField(('password'), max_length=128)
    last_login = models.DateTimeField(('last login'), blank=True, null=True) # дата и время послед активн в веб-прилож

    is_active = True

class AbstractUser(AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.

    Username and password are required. Other fields are optional.
    """
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        ('username'),
        max_length=150,
        unique=True,
        help_text=('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': ("A user with that username already exists."),
        },
    )
    first_name = models.CharField(('first name'), max_length=150, blank=True)
    last_name = models.CharField(('last name'), max_length=150, blank=True)
    email = models.EmailField(('email address'), blank=True)
    is_staff = models.BooleanField(
        ('staff status'),
        default=False,
        help_text=('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        ('active'),
        default=True,
        help_text=(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
date_joined = models.DateTimeField(('date joined'), default=timezone.now) # дата и время регистрац пользов

