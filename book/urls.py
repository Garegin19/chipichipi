from django.urls import path
from book import views

urlpatterns = [
    path('book/<int:pk>', views.BookList.as_view(), name='book_list')
]