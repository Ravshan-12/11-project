from django.urls import path
from . import views


app_name = 'news'


urlpatterns = [
    path('create/', views.news_create, name='create'),
    path('detail/<int:news_id>/', views.news_detail, name='detail'),
    path('category/<str:category>/', views.news_category, name='category'),
]