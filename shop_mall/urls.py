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
    path('/crewneck',views.crewneck, name="crewneck"),
    path('/pants',views.pants, name="pants"),
    path('/outer', views.outer, name="outer"),
    path('/accessories', views.accessories, name="accessories"),
]
