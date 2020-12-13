from django.urls import path
from todo_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_template, name='create_template'),
    path('create1/', views.create, name='create'),
    path('edit/<int:pk>', views.edit, name='edit'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('mark-done/<int:pk>', views.mark_todo_done, name='mark todo done')
]
