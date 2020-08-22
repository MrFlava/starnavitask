from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        print('New user is signed up')


@receiver(post_save, sender=User)
def create_post(sender, instance, created, **kwargs):
    if created:
        print('New post is created')


@receiver(post_save, sender=User)
def add_preference(sender, instance, created, **kwargs):
    if created:
        print('Preference added')

