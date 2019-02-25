from django.urls import path

from order import views

app_name = 'order'

urlpatterns = [
    path('submit_cart/', views.submit_cart, name='submit_cart'),
    path('creat_order/', views.creat_order, name='creat_order'),
    path('check_address/', views.check_address, name='check_address'),
]