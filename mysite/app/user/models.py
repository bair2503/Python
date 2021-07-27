from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from pytz import unicode


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user', null= True, blank=True)
    name = models.CharField(max_length=200, null= True, blank=True)
    iphone = models.CharField(max_length=200, null= True, blank=True)
    mail = models.CharField(max_length=200, null= True, blank=True)
    skype = models.CharField(max_length=200, null= True, blank=True)
    age = models.CharField(max_length=200, null= True, blank=True)
    address = models.CharField(max_length=200, null= True, blank=True)
    avatar = models.ImageField('logo', null=True, blank=True, upload_to='logo')
    def __str__(self):
        return unicode(self.id)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)