from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from app import views
 
urlpatterns = [
    path('admin', admin.site.urls),
    path('', views.index),
    re_path(r'^relevance', views.relevance),
    re_path(r'^geography', views.geography),
    re_path(r'^skills', views.skills),
    re_path(r'^last_vacansies', views.last_vacansies),
    re_path(r'', views.error)
]