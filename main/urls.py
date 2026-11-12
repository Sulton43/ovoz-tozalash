from django.urls import path
from .views import home_view, result_view

urlpatterns = [
    path('', home_view, name='home'),
    path('result/<int:pk>/', result_view, name='result'),
]