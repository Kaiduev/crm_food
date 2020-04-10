from django.contrib import admin

from .models import *

admin.site.register(Role)
admin.site.register(User)
admin.site.register(Status)
admin.site.register(Table)
admin.site.register(Department)
admin.site.register(MealCategory)
admin.site.register(Meal)
admin.site.register(Order)
admin.site.register(MealsToOrder)
admin.site.register(MealOrder)
admin.site.register(CheckOrder)
admin.site.register(CheckedMeal)


