from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    date = models.DateTimeField("date published", default=datetime.now())
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    objects = models.Manager()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about_yourself = models.TextField()
    avatar = models.ImageField(upload_to='profile_avatars/')

    objects = models.Manager()
