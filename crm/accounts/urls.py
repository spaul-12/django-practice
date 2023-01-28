from django.urls import path, include
from . import views

urlpatterns=[
    path('',views.home,name="home"),

    path('login/',views.loginUser,name="login"),
    path('accounts/',include('allauth.urls')),
    path('register/',views.register,name="register"),
    path('logout/',views.logoutuser,name="logout"),

    path('customer/<str:pk>/',views.customer,name="customer"),
    path('createorder/',views.createorder, name="create_order"),
    path('updateorder/<str:id>',views.updateorder,name="updateorder"),
    path('deleteorder/<str:pk>',views.deleteorder, name="deleteorder")

]