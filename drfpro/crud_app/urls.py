from django.urls import path
from . import views

urlpatterns = [
    path('student/',views.add_api),
    path('add/<int:pk>/',views.add_detial_api)
]