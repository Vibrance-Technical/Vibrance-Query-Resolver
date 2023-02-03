from django.urls import path
from . import views
urlpatterns = [
    path('create/query/',views.create_query,name = "create_query"),
    path('view/<slug:slug>/query/<int:pk>',views.QueryDetailView.as_view(),name = "query_detail_view"),
    path('approve/<slug:slug>/query/<int:pk>',views.approve_query,name = "approve_query"),
    path('reject/<slug:slug>/query/<int:pk>',views.reject_query,name = "reject_query"),
]