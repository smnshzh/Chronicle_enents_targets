from django.urls import path
from . import views
urlpatterns = [
    path("",views.dashboard,name="dashboard"),
    path ('flex', views.flex, name='flex'),
    path("pivot_data",views.pivot_data,name="pivot_data")
]