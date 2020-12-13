from django.urls import path

from recipes.views import homepage, create, edit, delete, details

urlpatterns = [
    path('', homepage, name='homepage'),
    path('create/', create, name='recipe create'),
    path('edit/<int:pk>', edit, name='recipe edit'),
    path('delete/<int:pk>', delete, name='recipe delete'),
    path('details/<int:pk>', details, name='recipe details'),
]
