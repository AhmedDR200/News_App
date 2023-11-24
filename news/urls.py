from django.urls import path
from . import views

urlpatterns =[
    path('list/', views.get_all_articles, name='all'),
    path('create/', views.create_article, name='create'),
    path('single/<int:id>/', views.single_article, name='single_article')
]