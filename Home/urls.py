#URL HOME
from django.urls import path
from Home.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),    
]
