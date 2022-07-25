from django.urls import path
from . import views
urlpatterns = [
    path ('dashboard', views.dashboard, name='dashboard'),
    path("pivot_data",views.pivot_data,name="pivot_data")
]