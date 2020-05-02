from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AnonymousUser, AbstractUser
from django.db import models
from user.models import User

from django.db import models


# class Role(models.Model):
#     name = models.CharField(max_length=255, unique=True)
#
#     class Meta:
#         ordering = ['name']
#
#     def __str__(self):
#         return self.name
#
#
# class User(AbstractUser):
#     name = models.CharField(max_length=255, unique=True)
#     surname = models.CharField(max_length=255)
#     login = models.CharField(max_length=255, unique=True)
#     email = models.EmailField(max_length=255, unique=True)
#     role = models.ForeignKey(
#         Role, on_delete=models.CASCADE, default=True, null=False)
#     date = models.DateTimeField(auto_now_add=True)
#     phone = models.CharField(max_length=255)
#
#     REQUIRED_FIELDS = ['email', 'role']
#     USERNAME_FIELD = 'name'
#
#     class Meta:
#         ordering = ['name']
#
#     def __str__(self):
#         return '{} {}'.format(self.name, self.role)


class Status(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Table(models.Model):
    name = models.CharField(max_length=150, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=150, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class MealCategory(models.Model):
    name = models.CharField(max_length=150)
    department = models.ForeignKey(Department, verbose_name='Department',
                                   on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Meal(models.Model):
    name = models.CharField(max_length=150)
    category = models.ForeignKey(MealCategory, verbose_name='MealCategory',
                                 on_delete=models.CASCADE)
    price = models.IntegerField()
    description = models.TextField(verbose_name=None, blank=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Order(models.Model):
    waiter = models.ForeignKey(User, on_delete=models.CASCADE, default=True, null=False)
    table = models.ForeignKey(Table, on_delete=models.CASCADE, default=True, null=False)
    isitopen = models.BooleanField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['waiter']

    def __str__(self):
        return self.table.name

    # def table_name(self):
    #     return self.table.name


class MealOrder(models.Model):
    order = models.ForeignKey(Order, verbose_name='order', on_delete=models.CASCADE, related_name='meals')
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, default=True, null=False)
    count = models.IntegerField()

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.meal.name

    def count_(self):
        return self.count


class MealsToOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE,
                              default=True, null=False)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.order


class CheckOrder(models.Model):
    ordername = models.CharField(max_length=150, default=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    servicefree = models.IntegerField(default=20)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.ordername

    def total_sum(self):
        return sum(item.total() for item in CheckedMeal.objects.filter(check_fk=self.id)) + self.servicefee


class CheckedMeal(models.Model):
    title = models.CharField(max_length=150, default='')
    mealorder = models.ForeignKey(
        MealOrder, on_delete=models.CASCADE, default=True, null=False, related_name='meals')
    check_fk = models.ForeignKey(
        CheckOrder, verbose_name='checkfk', on_delete=models.CASCADE, related_name='check_fk'
    )
    meal = models.ForeignKey(
        Meal, on_delete=models.CASCADE, default=True, null=False)

    def __str__(self):
        return self.title

    def name(self):
        return self.meal.name

    def amount(self):
        meal_id = self.meal
        return sum(item.get_count() for item in MealOrder.objects.filter(meal=meal_id))

    def price(self):
        return self.meal.price

    def total(self):
        price = self.price()
        amount = self.amount()
        return price * amount