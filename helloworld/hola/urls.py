from django.urls import path
from . import views
urlpatterns = [

    path('', views.home,name='home'),
    #path('hola/',views.abc,name='abc'),
]