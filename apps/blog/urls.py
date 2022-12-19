from django.urls import path

from . import views

app_name='blog'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('<slug>', views.Show, name='show'),
    path('category/<int:category_id>', views.category, name='category')
]