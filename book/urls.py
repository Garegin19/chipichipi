from django.urls import path
from book import views

urlpatterns = [
    path('book/', views.BookList.as_view(), name='book_list',),
    path('book/<int:pk>/', views.BookDetail.as_view(), name='book_id'),
]