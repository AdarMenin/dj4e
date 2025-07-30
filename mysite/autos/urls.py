from django.urls import path

from . import views

app_name = "autos"
"""app namespace for url reverse mapping (e.g autos:name_of_specific_path)
-> works on its own BUT you should include namespace="app_name" within the global urls.py file"""
urlpatterns = [
    path("", views.MainView.as_view(), name="all"),
    path("main/create/", views.AutoCreate.as_view(), name="auto_create"),
    path("main/<int:pk>/update/", views.AutoUpdate.as_view(), name="auto_update"),
    path("main/<int:pk>/delete/", views.AutoDelete.as_view(), name="auto_delete"),
    path("lookup/", views.MakeView.as_view(), name="make_list"),
    path("lookup/create/", views.MakeCreate.as_view(), name="make_create"),
    path("lookup/<int:pk>/update/", views.MakeUpdate.as_view(), name="make_update"),
    path("lookup/<int:pk>/delete/", views.MakeDelete.as_view(), name="make_delete"),
]
