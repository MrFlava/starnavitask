from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


app_name = "main"

urlpatterns = [
    path("posts", views.PostListCreateView.as_view(), name="add-post"),
    path("profile/<int:pk>", views.userProfileDetailView.as_view(), name="profile-activity"),
    path('post/<int:pk>', views.PostDetailView.as_view(), name=f'post'),
    path('postpreference', views.PreferenceCreateView.as_view(), name='add-postpreference'),
    path('postpreference-change/<int:pk>', views.ChangePreferenceView.as_view(), name='change-postpreference'),
    path('posts/likes-analysis', views.likesAnalysisView, name='likes-analysis')

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
