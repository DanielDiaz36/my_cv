from app import views
from app import settings
from django.urls import path
from django.contrib import admin


urlpatterns = [
    # path('admin/', admin.site.urls),

    path('', views.HomeView.as_view(), name='home'),
]
