from django.urls import path, include 
from .views import PostViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('posts', PostViewSet)

urlpatterns = [ 
    #path('get/',views.get_api),
    #path('post/', views.post_api),
    path('', include(router.urls))
]
