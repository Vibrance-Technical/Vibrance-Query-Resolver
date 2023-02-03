from django.urls import path
from . import views
urlpatterns = [
    path('create/query/',views.create_query,name = "create_query"),
]