from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ticket_book', views.ticket_book, name='ticket_book'),


]
