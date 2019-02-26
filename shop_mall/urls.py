from django.contrib import admin
from django.urls import path, include
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    #path('accounts/', include('allauth.urls')),
    path('/hoodie', views.hoodie, name="hoodie"),
    path('/hoodie/detail', views.detail, name="detail"),
    path('account/', include('account.urls')),
]
