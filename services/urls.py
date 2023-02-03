from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    #Auth
    path('login/',auth_views.LoginView.as_view(),name = "login"),
    path("logout/",auth_views.LogoutView.as_view(),name = "logout"),
    #CRUD
    path('create/query/',views.create_query,name = "create_query"),
    path('view/<slug:slug>/query/<int:pk>',views.QueryDetailView.as_view(),name = "query_detail_view"),
    path('approve/<slug:slug>/query/<int:pk>',views.approve_query,name = "approve_query"),
    path('reject/<slug:slug>/query/<int:pk>',views.reject_query,name = "reject_query"),
    path('view/',views.view_all_queries,name = "view_all_queries")
]