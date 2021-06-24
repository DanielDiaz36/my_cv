from django.urls import path
from django.contrib import admin
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.HomeView.as_view(), name='home'),
]
