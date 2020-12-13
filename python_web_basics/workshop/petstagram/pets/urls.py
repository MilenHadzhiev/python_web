from django.urls import path

from pets.views import landing_page, pets_all, pet_details, pet_like, create_pet, edit_pet, delete_pet

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('pets/', pets_all, name='all pets'),
    path('pets/details/<int:pk>', pet_details, name='pet details'),
    path('pets/like/<int:pk>', pet_like, name='pet like'),
    path('pets/create', create_pet, name='create pet'),
    path('pets/edit/<int:pk>', edit_pet, name='edit pet'),
    path('pets/delete/<int:pk>', delete_pet, name='delete pet'),
]
