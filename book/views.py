from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Count
from django.conf import settings

from .models import BookType,Book



def book_list_common(request, book_all):
    paginator = Paginator(book_all, settings.EACH_PAGE_BOOK_NUM)
    current_page_num = request.GET.get('page', 1)
    books = paginator.get_page(int(current_page_num))

    page_range = [page_num for page_num in range(int(current_page_num)-2, int(current_page_num)+3) if 0 < page_num <= paginator.num_pages]
    if page_range[0]-1 > 1:
        page_range.insert(0, '...')
    if page_range[-1]+1 < paginator.num_pages:
        page_range.append('...')
    if page_range[0] != 1:
        page_range.insert(0,1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)

    context = {}
    context['books'] = books
    context['page_range'] = page_range
    context['book_types'] = BookType.objects.annotate(book_count=Count('book'))

    return context


def book_list(request):
    book_all = Book.objects.all()
    context = book_list_common(request, book_all)
    return render(request, 'book_list.html', context)


def book_with_type(request, book_type_id):
    book_type = get_object_or_404(BookType, id=book_type_id)
    book_all = Book.objects.filter(book_type=book_type)

    context = book_list_common(request, book_all)
    context['book_type'] = book_type
    return render(request, 'book_with_type.html', context)


def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    context = {}
    context['book'] = book
    return render(request, 'book_detail.html', context)