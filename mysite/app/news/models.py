from django.db import models
from pytz import unicode


class News(models.Model):

    name = models.CharField(max_length=200)
    text= models.TextField(null= True, blank=True)



    def __str__(self):
        return unicode("+" + self.name)


class CreatNews(models.Model):
    category = models.ForeignKey(News, on_delete=models.CASCADE, null = True, blank = True)# тип помещает объект
    all_category = models.ManyToManyField(News, related_name= "all_category")# тип помещает объект
    name = models.CharField(max_length=200)
    text = models.TextField(null= True, blank=True)  # обязательно заполнять

    def __str__(self):
        return unicode("+" + self.name)