from rest_framework import viewsets, generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import Child, Blog, UserActivity
from .serializers import ChildSerializer, BlogSerializer, UserActivitySerializer
from rest_framework.permissions import IsAuthenticated
from django.core.cache import cache
from .filters import BlogFilter  # Import your custom filter
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers import ParentSerializer
from django.contrib.auth.models import User
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class ParentView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class =  ParentSerializer

class ChildViewSet(viewsets.ModelViewSet):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer
    # permission_classes = [IsAuthenticated]
    

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    # permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = BlogFilter  # Use the custom filter
    filterset_fields = ['age_group', 'tags']
    search_fields = ['title', 'content']

class UserActivityViewSet(viewsets.ModelViewSet):
    queryset = UserActivity.objects.all()
    serializer_class = UserActivitySerializer
    # permission_classes = [IsAuthenticated]

class PersonalizedFeedView(generics.ListAPIView):
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('Authorization', openapi.IN_HEADER, description="Authorization header", type=openapi.TYPE_STRING),
            openapi.Parameter('parent_id', openapi.IN_QUERY, description="Parent ID", type=openapi.TYPE_INTEGER)
        ]
    )    
    def get_queryset(self):
        parent = User.objects.get(id=self.request.GET.get("parent_id", 1))
        key = f'personalized_feed_{parent.id}'
        cached_feed = cache.get(key)
        if cached_feed:
            return cached_feed

        children = Child.objects.filter(parent=parent)
        print("children")
        print("children")
        print(children)
        child_ages = [child.age for child in children]
        interests = [activity.blog.tags for activity in UserActivity.objects.filter(user=parent)]
        interests = [tag for sublist in interests for tag in sublist]
        print("interests")
        print(interests)

        queryset = Blog.objects.filter(age_group__in=child_ages).order_by('-created_at')
        queryset |= Blog.objects.filter(tags__overlap=interests).order_by('-views')

        cache.set(key, queryset, timeout=300)  # Cache for 5 minutes
        return queryset
