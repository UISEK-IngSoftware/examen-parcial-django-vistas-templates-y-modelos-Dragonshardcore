from django.urls import path
from . import views



urlpatterns = [
    path("", views.index, name="index"),
    path('movie/<int:movie_id>/', views.movie_detail, name='movie_details'),
    path('ajax/movie/<int:movie_id>/', views.movie_details_ajax, name='movie_details_ajax'),

]

