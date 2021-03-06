from django.conf.urls import url
from django.urls import path
from .views import *

urlpatterns = [
    path('tables/', TableView.as_view()),
    path('tables/<int:pk>/',TableDetail.as_view()),
    path('roles/', RoleView.as_view()),
    path('roles/<int:pk>/', RoleDetail.as_view()),
    path('departments/', DepartmentView.as_view()),
    path('departments/<int:pk>/', DepartmentDetail.as_view()),
    path('users/', UserView.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('meal/categories/', MealCategoryView.as_view()),
    path('meal/categories/<int:pk>/', MealCategoryDetail.as_view()),
    path('statuses/', StatusView.as_view()),
    path('statuses/<int:pk>/', StatusDetail.as_view()),
    path('meals/', MealView.as_view()),
    path('meals/<int:pk>/',MealDetail().as_view()),
    path('mealsbycategory/', MealsByCategory.as_view()),
    path('orders/', OrderView.as_view()),
    path('orders/<int:pk>/', OrderDetail.as_view()),
    path('orders/active/', ActiveOrders.as_view()),
    path('checks/', CheckView.as_view()),
    path('checks/<int:pk>/', CheckDetail.as_view()),
]
