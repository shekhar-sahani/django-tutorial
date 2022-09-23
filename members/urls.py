from django.urls import path
from .views import greet_user, index, add, addrecord, delete, update, updaterecord

urlpatterns = [
    path('', index, name='index'),
    path('add/', add, name='add'),
    path('add/addrecord/', addrecord, name='addrecord'),
    path('delete/<int:id>', delete, name='delete'),
    path('update/<int:id>', update, name='update'),
    path('update/updaterecord/<int:id>', updaterecord, name='updaterecord'),
    path('user', greet_user, name='user_greet')
]