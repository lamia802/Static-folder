from django.urls import path
from .views import get_all, about , update , delete
urlpatterns = [
    path("get-all/", get_all, name="index"),
    path("about/", about, name="about" ),
    path("delete/<int:id>/", delete, name="delete" ),
    path("update/<int:id>/<str:title>/<str:describtion>/", update, name="update"),
]