from django.urls import path
from . import views

app_name = "flights"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:flight_id>/", views.detail, name="detail"),
    path("<int:flight_id>/vote/", views.vote, name="vote"),
    path("<int:flight_id>/results/", views.results, name="results"),
]
