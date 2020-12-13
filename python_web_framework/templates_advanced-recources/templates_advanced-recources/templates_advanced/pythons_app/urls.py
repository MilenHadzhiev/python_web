from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name="create"),
    path('<int:pk>/', views.python_details, name='python detail'),
    path('<int:pk>/<path:slug>/', views.python_details, name='python detail'),
    path('register/', views.register_user, name='register user'),
    path('login/', views.login_user, name='login user'),
    path('logout/', views.logout_user, name='logout user'),
    path('unauthorized/', views.unauthorized, name='unauthorized'),
]
