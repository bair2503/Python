from django.db import models
from pytz import unicode


class Information(models.Model):

    name = models.CharField(max_length=200)


    def __str__(self):
        return unicode("+" + self.name)

class ElementInformation(models.Model):
    information = models.ForeignKey(Information, on_delete=models.CASCADE, null = True, blank = True)
    logo = models.ImageField('logo', null=True, blank=True, upload_to='logo')
    logo_width = models.IntegerField(default=0)
    logo_height = models.IntegerField(default=0)
    text = models.TextField(null=True, blank=True)


    def __str__(self):
        return unicode(self.id)