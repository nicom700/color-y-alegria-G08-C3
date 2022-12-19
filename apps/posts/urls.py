from django.urls import path
from django.conf.urls.static import static #For media conf
from django.conf import settings #For media conf

from . import views

app_name='posts'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('create/', views.Create, name='create'),
    path('edit/<int:pk>', views.Edit, name='edit'),
    path('delete/<int:pk>', views.Delete.as_view(), name='delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # For media conf
