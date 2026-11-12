from django.urls import path
from .views import home_view, result_view, recordings_view

urlpatterns = [
    path('', home_view, name='home'),
    path('result/<int:pk>/', result_view, name='result'),
    path('recordings/', recordings_view, name='recordings'),
]