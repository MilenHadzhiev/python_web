from django.contrib import admin
from django.urls import path, include

from urls_and_templates import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_page),
    path('main_app/', include('main_app.urls')),
    path('secondary_app/', include('secondary_app.urls'))
]
