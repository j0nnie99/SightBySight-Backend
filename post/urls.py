from django.urls import path, include 
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('posts', views.PostViewSet)

urlpatterns = [ 
    path('list/',views.postList),
    #path('post/', views.post_api),
    path('', include(router.urls)),
    path('myPost/', views.viewMyPost),
    
]
