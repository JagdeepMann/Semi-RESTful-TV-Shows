from django.urls import path, include
from restful_app import views

urlpatterns = [
    path('', views.index),
    path('shows/', include('restful_app.urls')),
]