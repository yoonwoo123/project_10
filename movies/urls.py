from django.urls import path
from rest_framework_swagger.views import get_swagger_view
from . import views

urlpatterns = [
    path('docs/', get_swagger_view(title="영화 정보 API")),
    path('genres/', views.genre_list),
    path('genres/<int:genre_pk>/', views.genre_detail),
    path('movies/', views.movie_list),
    path('movies/<int:movie_pk>/', views.movie_detail),
    path('movies/<int:movie_pk>/scores/', views.score_new),
    path('scores/<int:movie_pk>/<int:score_pk>/', views.score_edit_delete),
]
