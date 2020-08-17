from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


app_name = "main"

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_request, name='logout'),
    path('login/', views.login_request, name='login'),
    path('add_profile_info/', views.add_profile_info, name='add_profile'),
    path('edit_profile/', views.edit_profile_info, name='edit_profile'),
    path('profile/', views.show_profile, name='profile'),
    path('create_a_post/', views.create_a_post, name='create_a_post'),
    path('post/<int:pk>/', views.show_post, name=f'post'),
    path('post/<int:pk>/like', views.like_post, name='like_post'),
    path('post/<int:pk>/dislike', views.dislike_post, name='dislike_post'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
