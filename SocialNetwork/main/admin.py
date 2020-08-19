from django.contrib import admin
from .models import Post, Preference, UserActivity

# Register your models here.
admin.site.register(Post)
admin.site.register(Preference)
admin.site.register(UserActivity)