from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from book.forms import BookForm
from book.models import Book


def index(request):
    books = Book.objects.all()
    context = {
        'books': books,
    }
    return render(request, 'index.html', context)


def initialize_book(book_form, pk=None):
    if pk:
        book = Book.objects.get(pk=pk)
        book.title = book_form.cleaned_data['title']
        book.pages = book_form.cleaned_data['pages']
        book.description = book_form.cleaned_data['description']
        book.author = book_form.cleaned_data['author']
    else:
        title = book_form.cleaned_data['title']
        pages = book_form.cleaned_data['pages']
        description = book_form.cleaned_data['description']
        author = book_form.cleaned_data['author']
        book = Book(
            title=title,
            pages=pages,
            description=description,
            author=author,
        )
    book.save()
    return redirect(index)


def create(request, book_form=None, form_action='create_book', pk=None):
    if not book_form:
        book_form = BookForm()
    context = {
        'book_form': book_form,
        'form_action': form_action,
        'pk': pk,
    }
    return render(request, 'create.html', context)


@require_POST
def create_book(request):
    book_form = BookForm(request.POST)
    if book_form.is_valid():

        return initialize_book(book_form)

    return create(request, book_form=book_form)


def edit(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'GET':
        book_form = BookForm(initial=book.__dict__)
        return create(request, book_form, 'edit', pk=pk)
    else:
        book_form = BookForm(request.POST)
        if book_form.is_valid():
            initialize_book(book_form, pk)
            return redirect(index)
        return create(
            request,
            book_form=book_form,
            form_action='edit',
            pk=pk
        )


def delete(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return redirect(index)
