from django.urls.conf import path,include
from .views import HomeView

app_name='feed'
urlpatterns= [
    path('',HomeView.as_view(),name='home'),
    
]