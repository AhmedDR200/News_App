from django.urls import path
from . import views

urlpatterns =[
    path('list/', views.get_all_articles, name='all'),
    path('create/', views.create_article, name='create'),
    path('single/<int:id>/', views.single_article, name='single_article'),
    path('list_class/', views.ArticleListCreate.as_view(), name="list_class"),
    path('detail_class/<int:pk>', views.ArticleDetail.as_view(), name="detail_class"),
    path('journalist_list/', views.get_all_journalists, name="get_all_journalists"),
    path('create_journalist/', views.create_journalist, name="create_journalist"),
]