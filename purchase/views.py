from django.shortcuts import render,get_object_or_404,redirect
from django.db.models import F,ExpressionWrapper,Sum
from django.db import models
from django.urls import reverse
from .models import ShoppingCart
from book.models import Book


def add_to_shopping_cart(request):
    book_id = request.GET.get('book_id')
    book = get_object_or_404(Book, id=book_id)
    user = request.user
    if ShoppingCart.objects.filter(book=book, user=user).exists():
        book_in_cart = ShoppingCart.objects.get(book=book, user=user)
        book_in_cart.book_num += 1
    else:
        book_in_cart = ShoppingCart()
        book_in_cart.book = book
        book_in_cart.user = user   
    book_in_cart.save()
    return redirect(reverse('shopping_cart'))

def remove_from_shopping_cart(request):
    book_id = request.GET.get('book_id')
    book = get_object_or_404(Book, id=book_id)
    user = request.user
    book_in_cart = ShoppingCart.objects.get(book=book, user=user)
    book_in_cart.delete()       
    return redirect(reverse('shopping_cart'))



def shopping_cart(request):
    context = {}
    context['books_in_cart'] = ShoppingCart.objects.filter(user=request.user) \
                                .annotate(one_book_money=ExpressionWrapper(F('book__price') * F('book_num'), output_field=models.DecimalField()))
    context['total_money'] = ShoppingCart.objects.filter(user=request.user) \
                                .aggregate(total=Sum(F('book__price') * F('book_num'), output_field=models.DecimalField()))['total']
    return render(request, 'shopping_cart.html', context)


def confirm_order(request):
    context = {}
    context['books_is_buying'] = ShoppingCart.objects.filter(user=request.user, is_selected=True) \
                                .annotate(one_book_money=ExpressionWrapper(F('book__price') * F('book_num'), output_field=models.DecimalField()))
    context['total_money'] = ShoppingCart.objects.filter(user=request.user, is_selected=True) \
                                .aggregate(total=Sum(F('book__price') * F('book_num'), output_field=models.DecimalField()))['total']
    return render(request, 'confirm_order.html', context)
    