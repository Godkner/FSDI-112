from django.urls import path
from .views import PostListView,PostDetailView,PostCreateView,PostDeleteView, PostUpdateView

urlpatterns = [
    path('',PostListView.as_view(), name="list"),
    path("<int:pk>/", PostDetailView.as_view(),name="detail"),
    path("new/",PostCreateView.as_view(),name="new"),
    path("<int:pk>/update/", PostUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", PostDeleteView.as_view(), name="delete"),
]