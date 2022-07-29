from django.urls import path
from . import views
urlpatterns = [
    path ('insert_targets', views.insert_targets, name='insert_targets'),
    path('data',views.makedata,name='data'),
    path('center_targets_definde',views.center_targets_definde,name="center_target_definde")
]