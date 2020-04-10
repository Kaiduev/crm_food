from django.urls import path
from .views import *

urlpatterns = [
    path('tables/', TableView.as_view()),
    path('tables/<int:pk>/',TableDetail.as_view())
]
