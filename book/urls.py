from django.urls import path
from book import views

urlpatterns = [
    path('book', views.BookList.as_view(), name='book_list'),
    path('book/<int:pk>', views.BookDetail.as_view(), name='book_id'),
    path('book/<int:pk>/date', views.GetDateForBook.as_view()),
    path('book/dates', views.GetDate.as_view()),
    path('book/search', views.SearchBook.as_view()),
    path('book/order', views.OrderDate.as_view())
]