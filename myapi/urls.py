from django.urls import path,include
from . import views
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'Member', views.MemberViewSet)



urlpatterns = [
    path('employees', views.home, name='home',),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
   
    path('', include(router.urls)),
]
