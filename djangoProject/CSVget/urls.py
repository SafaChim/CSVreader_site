from django.urls import path
from . import views

app_name = "CSVget"
urlpatterns = [
    path("", views.check, name="check"),
    path("add", views.add, name="add")
]