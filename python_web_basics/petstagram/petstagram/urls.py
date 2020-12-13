from django.contrib import admin
from django.urls import path, include

from petstagram import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('common.urls')),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('pets/', views.pet_list, name='pet list'),
    path('pets/details/<int:pk>', views.pet_detail, name='pet detail'),
    path('pets/like/<int:pk>', views.like_pet, name='like pet')
]
