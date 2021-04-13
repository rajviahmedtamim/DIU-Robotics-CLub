from django.urls import path
from .views import Home, Contact,Singleproject,Multipleproject,Aboutus
urlpatterns = [
    path('',Home, name='home'),
    path('contact/',Contact, name='Contact'),
    path('project/<int:id>/',Singleproject, name='singleproject'),
    path('multipleproject/',Multipleproject, name='Multipleproject'),
    path('about/',Aboutus, name='aboutus'),
]