from django.shortcuts import render
from .models import Book

CONTENT = [item[0] for item in set(Book.objects.values_list('pub_date'))]
CONTENT.sort()

def books_view(request):
    template = 'books/books_list.html'
    context = {'books': Book.objects.all()}
    return render(request, template, context)

def books_date_view(request, date):
    template = 'books/books_list_date.html'
    format = '%Y-%m-%d'
    date = date.date()
    next_lost_date = []
    if CONTENT.index(date) != len(CONTENT) - 1 and CONTENT.index(date) != 0:
        next_lost_date.append(str(CONTENT[CONTENT.index(date) - 1]))
        next_lost_date.append(str(CONTENT[CONTENT.index(date) + 1]))
    elif CONTENT.index(date) == len(CONTENT) - 1:
        next_lost_date.append(str(CONTENT[CONTENT.index(date) - 1]))
    elif CONTENT.index(date) == 0:
        next_lost_date.append(str(CONTENT[CONTENT.index(date) + 1]))
    context = {'books': Book.objects.filter(pub_date=date),
               'next_lost_date': next_lost_date}
    return render(request, template, context)

def book_view(request, slug):
    template = 'books/book.html'
    context = {'book': Book.objects.get(slug=slug)}
    return render(request, template, context)
