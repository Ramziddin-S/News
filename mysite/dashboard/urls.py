from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_page, name="dashboard"),
    path('login/', views.dashboard_login, name="login"),
    path('logout/', views.dashboard_logout, name="logout"),

    path('category/list/', views.category_list, name="category_list"),
    path('category/add/', views.category_create, name="category_add"),

    path('news/list/', views.news_list, name="news_list"),
    path('news/add/', views.news_create, name="news_add"),
    path('news/<int:news_id>/delete/', views.delete_news,name="delete_news"),

    path('authors/list/', views.authors_list, name="authors_list"),
    path('authors/add/', views.authors_create, name="authors_add"),

    path('references/list/', views.references_list, name="references_list"),
    path('references/add/', views.references_create, name="references_add"),

]
