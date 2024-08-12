from django.urls import path
from app import views

urlpatterns = [
    path('register',views.register, name="register"),
    path('login',views.loginPage, name="login"),
    path('logout',views.loginPage, name="logout"),

    path('',views.index, name="index"),
    path('about',views.about, name="about"),
    path('insert', views.insertData, name="intertData"),
    path('update/<id>', views.updateData, name="updateData"),
    path('delete/<id>', views.deleteData, name="deleteData"),
]
