from django.urls import path
from . import views
urlpatterns = [
    path ('/goodsinput', views.product_insert, name='product'),
    path ('/group', views.group_insert, name='group')
]