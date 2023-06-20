from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("simplecalc", views.simplecalc, name="simplecalc"),
    path("about", views.about, name="about"),
    path("marketchart", views.marketchart, name="marketchart"),
]