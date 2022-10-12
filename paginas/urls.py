from ast import Index
from django.urls import path
from .views import IndexView


urlpatterns = [
    path('',IndexView.as_view(), name='inicio'),
    # path('endereco/',MinhaView.as_view(), name='nomedaurl')
]
