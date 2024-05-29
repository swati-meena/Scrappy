from django.urls import path, include
from . import views

urlpatterns = [
    path('scrape/', views.scrape, name="scrape"),
    
]
