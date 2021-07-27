from django.contrib.auth.models import User
from django.db import models
from pytz import unicode


class Category(models.Model):

    name = models.CharField(max_length=200)
    number = models.IntegerField(default=0)
    descripshion = models.TextField(null= True, blank=True)
    viziboll = models.BooleanField(default= True)
    prace = models.FloatField(default=0)

    def __str__(self):
        return unicode("+" + self.name)



class Article(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null = True, blank = True)# тип помещает объект
    logo = models.ImageField('logo', null=True, blank=True, upload_to='logo')
    logo_width = models.IntegerField(default = 0)
    logo_height = models.IntegerField(default = 0)
    all_category = models.ManyToManyField(Category, related_name= "all_category")# тип помещает объект
    name = models.CharField(max_length=200)
    text = models.TextField(null= True, blank=True)  # обязательно заполнять

    def __str__(self):
        return unicode("+" + self.name)



class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null = True, blank = True)# тип помещает объект
    text = models.TextField(null= True, blank=True)  # обязательно заполнять
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True)
    def __str__(self):
        return unicode (str(self.id))


class Presents(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null = True, blank = True)# тип помещает объект
    text = models.TextField(null= True, blank=True)  # обязательно заполнять
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True)
    def __str__(self):
        return unicode (str(self.id))




