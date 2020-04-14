from django.urls import path
from .views import *

urlpatterns = [
    path('tables/', TableView.as_view()),
    path('tables/<int:pk>/',TableDetail.as_view()),
    path('roles/', RoleView.as_view()),
    path('roles/<int:pk>/', RoleDetail.as_view()),
    path('departments/', DepartmentView.as_view()),
    path('departments/<int:pk>/', DepartmentDetail.as_view()),
]
