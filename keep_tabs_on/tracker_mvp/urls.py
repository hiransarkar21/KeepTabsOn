from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name="tracker_index")
]
