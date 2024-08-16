# # blog/views.py
# from rest_framework import viewsets
# from .models import Post
# from .serializers import PostSerializer
# from rest_framework import filters

# class PostViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all().order_by('-published_date')
#     serializer_class = PostSerializer
#     filter_backends = [filters.SearchFilter, filters.OrderingFilter]
#     search_fields = ['title', 'content']
#     ordering_fields = ['created_date', 'published_date']

#     def get_queryset(self):
#         # queryset = Post.objects.all().order_by('-published_date')
#         queryset = super().get_queryset()
#         category = self.request.query_params.get('category', None)
#         if category is not None:
#             queryset = queryset.filter(category=category)
#         return queryset

from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer
from rest_framework import filters

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-published_date')
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'content']
    ordering_fields = ['created_date', 'published_date']

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.query_params.get('category', Post.BLOG)  
        queryset = queryset.filter(category=category)
        return queryset
class ReviewPostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-published_date')
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'content']
    ordering_fields = ['created_date', 'published_date']

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.query_params.get('category', Post.REVIEW)  # Default to 'blog'
        queryset = queryset.filter(category=category)
        return queryset