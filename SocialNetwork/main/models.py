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


class UserActivity(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_visit = models.DateTimeField(default=datetime.now())
    last_request = models.DateTimeField(default=datetime.now())

    objects = models.Manager()


class Preference(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.IntegerField()
    date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return str(self.user) + ':   ' + str(self.post) + ':' + str(self.value)

    class Meta:
        unique_together = ("user", "post", "value")

    objects = models.Manager()
