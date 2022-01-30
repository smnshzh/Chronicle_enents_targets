from django.urls import path
from . import views
urlpatterns = [
    path ('saleinfo', views.saleInfo, name='saleInfo'),
]