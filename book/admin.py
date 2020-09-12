from django.contrib import admin
from .models import Book,BookType


@admin.register(BookType)
class BookTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name')
    ordering = ('-id',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'book_number', 'book_name', 'book_type', 'price', \
                    'author', 'publishing_house', 'publishing_time', 'storage_time', 'warehouse_operator', 'content')
    ordering = ('-id',)
