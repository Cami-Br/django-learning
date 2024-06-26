from django.urls import path

from meetings import views


urlpatterns = [
    path("<int:id>", views.details, name="details"),
    path("rooms", views.rooms, name="rooms"),
    path("new", views.new, name="new"),
    path('edit/<int:id>', views.edit, name="edit"),
    path('delete/<int:id>', views.delete, name="delete")
]
