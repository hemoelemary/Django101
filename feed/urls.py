from django.urls.conf import path,include
from .views import HomeView,Details,AddPost

app_name='feed'
urlpatterns= [
    path('',HomeView.as_view(),name='home'),   
    path('detail/<int:pk>/',Details.as_view(),name='details'),
    path('post/',AddPost.as_view(),name='post')
]