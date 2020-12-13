from django.urls import path

from expenses_tracker.views import homepage, expense_create, expense_edit, expense_delete, profile, profile_edit, \
    profile_delete

urlpatterns = [
    path('', homepage, name='home page'),
    path('create/', expense_create, name='expense create'),
    path('edit/<int:pk>', expense_edit, name='expense edit'),
    path('delete/<int:pk>', expense_delete, name='expense delete'),
    path('profile/', profile, name='profile page'),
    path('profile/edit/', profile_edit, name='profile edit'),
    path('profile/delete/', profile_delete, name='profile delete')
]
