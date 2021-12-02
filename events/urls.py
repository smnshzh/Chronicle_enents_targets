from django.urls import path

from . import views
urlpatterns = [
    path ('', views.index, name='index'),
    path ('login', views.logIn, name='login'),
    path ('logout', views.out, name='logout'),
    path ('eventViewer',views.eventView,name = 'eventView'),
    path ('insertEvent',views.insertEvent,name='insertEvent'),
    path ('deletEvent<int:id>',views.deleteEvent,name = 'deletEvent'),
    path('acceptEvent',views.acceptEvent,name='acceptEvent'),

]