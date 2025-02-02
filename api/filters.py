import django_filters
from django_filters import rest_framework as filters
from django.db.models import JSONField
from .models import Blog

class BlogFilter(filters.FilterSet):
    tags = filters.CharFilter(method='filter_tags')  # Custom method to filter JSONField

    class Meta:
        model = Blog
        fields = ['title', 'tags']

        # ✅ Override JSONField filtering to allow filtering JSON data
        filter_overrides = {
            JSONField: {
                "filter_class": filters.CharFilter,
            },
        }

    def filter_tags(self, queryset, name, value):
        """
        Custom filter function to filter JSONField data
        """
        return queryset.filter(**{f"{name}__icontains": value})
