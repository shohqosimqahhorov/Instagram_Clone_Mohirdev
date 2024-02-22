from django.urls import path
from .views import PostListApiView, PostCreateView, \
    PostRetrieveUpdateDeleteView, PostCommentListView, PostCommentCreateView, \
    CommentListCreateView, PostLikeListView, CommentRetrieveView, \
    CommentLikeListView, PostLikeApiView,CommentLikeApiView

urlpatterns = [
    path('list/', PostListApiView.as_view()),
    path('create/', PostCreateView.as_view()),
    path('<uuid:pk>/', PostRetrieveUpdateDeleteView.as_view()),
    path('<uuid:pk>/likes/', PostLikeListView.as_view()),
    path('<uuid:pk>/comments/', PostCommentListView.as_view()),
    path('<uuid:pk>/comments/create/', PostCommentCreateView.as_view()),

    path('comments/', CommentListCreateView.as_view()),
    path('comments/<uuid:pk>/', CommentRetrieveView.as_view()),
    path('comments/<uuid:pk>/likes/', CommentLikeListView.as_view()),

    path('<uuid:pk>/create-delete-like/', PostLikeApiView.as_view()),
    path('comments/<uuid:pk>/create-delete-like/', CommentLikeApiView.as_view()),

]
