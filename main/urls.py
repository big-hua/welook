from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path('bookdetail/', views.bookdetail, name='bookdetail'),
    path('index/', views.arrive_index, name='index'),
    path('query/',views.query_category_book, name='query')
]