from django.contrib import admin
from django.urls import path
from progress_tracking import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.dashboard, name="dashboard"),

    # Progress CRUD
    path("progress/", views.progress_list, name="progress_list"),
    path("progress/add/", views.progress_create, name="progress_create"),
    path("progress/<int:pk>/edit/", views.progress_update, name="progress_update"),
    path("progress/<int:pk>/delete/", views.progress_delete, name="progress_delete"),

    # Blog
    path("blogs/", views.blog_list, name="blog_list"),
    path("blogs/add/", views.blog_create, name="blog_create"),
    path("blogs/<int:pk>/", views.blog_detail, name="blog_detail"),
    path("blogs/<int:pk>/edit/", views.blog_update, name="blog_update"),
    path("blogs/<int:pk>/delete/", views.blog_delete, name="blog_delete"),
]
