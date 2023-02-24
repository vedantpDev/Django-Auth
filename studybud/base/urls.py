# this is for any specific  app


from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='room'),
    path('contact', views.contact, name='contact'),
    path('services', views.services, name='services')
]
