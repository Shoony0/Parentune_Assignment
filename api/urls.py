from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from api.views import ChildViewSet, BlogViewSet, UserActivityViewSet, PersonalizedFeedView, ParentView


# Router for ViewSets
router = DefaultRouter()
router.register(r'parent', ParentView, basename="parent")
router.register(r'children', ChildViewSet, basename="children")
router.register(r'blogs', BlogViewSet, basename="blogs")
router.register(r'activities', UserActivityViewSet, basename="activities")

urlpatterns = [
    # path('register/parent/', UserCreateView.as_view(), name='parent-register'),
    path('personalized-feed/', PersonalizedFeedView.as_view(), name='personalized-feed'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]
