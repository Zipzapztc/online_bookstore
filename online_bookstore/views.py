from django.shortcuts import render
from django.db.models import Q
from book.models import Book
from book.views import book_list_common

def home(request):
    context = {}   
    return render(request, 'home.html', context)


def search(request):
    search_word = request.GET.get('search_word','').strip()
    condition = None
    for word in search_word.split(' '):
        if condition is None:
            condition = Q(book_name__icontains=word) | Q(author__icontains=word) | Q(publishing_house__icontains=word)
        else:
            condition = condition | Q(book_name__icontains=word) | Q(author__icontains=word) | Q(publishing_house__icontains=word)

    if condition is not None:        
        search_books = Book.objects.filter(condition)
    else:
        search_books = Book.objects.all()

    context = book_list_common(request,search_books)
    context['search_word'] = search_word
    context['search_books_count'] = search_books.count()
    return render(request, 'search.html', context)
