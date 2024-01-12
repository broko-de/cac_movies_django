from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('', views.index,name='inicio_app'),
    path('api/movies/', views.get_movies,name='getmovies_app'),
    path('api/create_movie/', views.create_movie),
    path('api/movies/<int:id>/', views.detail_movie),
    path('api/delete_movie/<int:id>/', views.detele_movie),
    path('api/update_movie/<int:id>/', views.update_movie),
]