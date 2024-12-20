from django.urls import path
from . import views

urlpatterns = [
    # List all microcontrollers
    path("microcontrollers/", views.all_microcontrollers,
          name="all_microcontrollers"),
    # View details of a specific microcontroller
    path(
        "microcontroller/<int:microcontroller_id>/",
        views.microcontroller_detail,
        name="microcontroller_detail",
    ),
    # Add a new microcontroller
    path("add-microcontroller/", views.add_microcontroller,
          name="add_microcontroller"),
    # Edit an existing microcontroller
    path(
        "edit-microcontroller/<int:microcontroller_id>/",
        views.edit_microcontroller,
        name="edit_microcontroller",
    ),
    # Delete a microcontroller
    path(
        "delete-microcontroller/<int:microcontroller_id>/",
        views.delete_microcontroller,
        name="delete_microcontroller",
    ),
]
