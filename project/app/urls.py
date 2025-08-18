from django.urls import path
from .views import (
    LoginAPIView,
    CategoryListCreateView,
    ProfileView,
    ProductListView,
    ProductCreateView,
    ProductDetailView,
    ProductImageUploadView,
    TagListView,
    TagCreateView,
)

urlpatterns = [
    path("login/", LoginAPIView.as_view()),

    path("categories/", CategoryListCreateView.as_view()),

    path("profile/", ProfileView.as_view()),

    path("tags/", TagListView.as_view()),
    path("tags/create/", TagCreateView.as_view()),

    path("products/", ProductListView.as_view()),
    path("products/create/", ProductCreateView.as_view()),
    path("products/<int:pk>/", ProductDetailView.as_view()),

    path("products/<int:pk>/upload-image/", ProductImageUploadView.as_view()),
]