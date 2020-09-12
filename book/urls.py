from django.urls import path
from .views import book_list,book_with_type,book_detail


#http://localhost:8000/book/
urlpatterns = [
    path('', book_list, name='book_list'),
    path('<int:book_id>', book_detail, name='book_detail'),
    path('type/<int:book_type_id>', book_with_type, name='book_with_type'),
    
]