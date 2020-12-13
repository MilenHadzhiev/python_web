from django.urls import path

from book.views import index, create, edit, create_book, delete

urlpatterns = [
    path('', index, name='index'),
    path('create/', create, name='create'),
    path('create-book/', create_book, name='create_book'),
    path('edit/<int:pk>', edit, name='edit'),
    path('delete/<int:pk>', delete, name='delete')
]
