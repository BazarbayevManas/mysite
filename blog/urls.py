from django.conf.urls import url
from django.urls import path
from . import views
from .feeds import LatestPostFeed

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    # path('', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    url(r'^(?P<post_id>\d+)/share/$', views.post_share, name='post_share'),
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
    path('feed/', LatestPostFeed(), name='post_feed'),
]
