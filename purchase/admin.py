from django.contrib import admin
from .models import ShoppingCart

@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'book_num', 'user', 'is_selected')
    ordering = ('-id',)


