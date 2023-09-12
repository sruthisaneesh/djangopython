from .import views
from django.urls import path

urlpatterns = [

    path('',views.index,name='index'),
    # path('operations/',views.addition,name='addition'),



]
