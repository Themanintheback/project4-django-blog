from django.urls import path
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article_detail'),
    path('add_posts/', AddPostView.as_view(), name='add_posts'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post')
]