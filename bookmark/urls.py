from django.urls import path

from bookmark.views import BookmarkListView, BookmarkCreateView, BookmarkModifyView, BookmarkDetailView, \
    BookmarkDeleteView

app_name = 'bookmark'
urlpatterns = [
    path('', BookmarkListView.as_view(), name='index'),
    path('add/', BookmarkCreateView.as_view(), name='create'),
    path('update/<int:pk>', BookmarkModifyView.as_view(), name='update'),
    path('detail/<int:pk>', BookmarkDetailView.as_view(), name='detail'),
    path('delete/<int:pk>', BookmarkDeleteView.as_view(), name='delete'),
]