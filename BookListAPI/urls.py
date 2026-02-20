from django.urls import path, include
from . import views


urlpatterns = [
    # path('books/', views.books, name='books'),
    # path('books/', views.BookList.as_view()),
    path('books/', views.BookView.as_view()),
    path('books/<int:pk>', views.SingleBookView.as_view()),
    path('__debug__/', include('debug_toolbar.urls')),
]
