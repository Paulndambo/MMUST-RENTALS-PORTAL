from django.urls import path
from .import views 

urlpatterns = [
    path("", views.home, name="home"),
    path("owners/", views.hostel_owners, name="owners"),
    path("owner/", views.CreateOwner.as_view(), name="owner"),
    path("owner/<int:pk>/", views.UpdateOwner.as_view(), name="edit-owner"),
    path("owner-details/<int:pk>/", views.OwnerDetails.as_view(), name="owner-details"),
    path("hostels/", views.hostels, name="hostels"),
    path("students/", views.students, name="students"),
]


