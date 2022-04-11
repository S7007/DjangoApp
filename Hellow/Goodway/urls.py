from django.contrib import admin
from django.urls import path , include
from Goodway import views

urlpatterns = [
    path("",views.index, name = 'home'),
    path("about",views.about, name = 'about'),
    path("services",views.services, name = 'services'),
    path("contact",views.contact, name = 'contact'),
    path("cobing",views.cobing, name = 'cobing'),
    path("shopping",views.shopping, name = 'shopping'),
    path("novel",views.novel, name = 'novel'),
    path("videoc",views.videoc, name = 'videoc'),





    

]

