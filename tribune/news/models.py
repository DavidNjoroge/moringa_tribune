from django.db import models
import datetime as dt
from tinymce.models import HTMLField
from django.contrib.auth.models import User
# Create your models here.
# class Editor(models.Model):
#     first_name=models.CharField(max_length=30)
#     last_name=models.CharField(max_length=32)
#     email=models.EmailField()
#     phone_number = models.CharField(max_length = 10,blank =True)
#
#     def __str__(self):
#         return self.first_name
#
#     def save_editor(self):
#         self.save()
#
#     def del_editor(self):
#         self.delete()
#
#
#     class Meta:
#         ordering=['first_name']

class tags(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Article(models.Model):
    title=models.CharField(max_length=60)
    post=HTMLField()
    editor = models.ForeignKey(User,on_delete=models.CASCADE)
    tag=models.ManyToManyField(tags)
    pub_date=models.DateTimeField(auto_now_add=True)
    article_image=models.ImageField(upload_to='articles/')

    def save_article(self):
        self.save()
    @classmethod
    def todays_news(cls):
        today=dt.date.today()
        news=cls.objects.filter(pub_date__date=today)   
        return news
    @classmethod
    def days_news(cls,date):
        print(date)

        news=cls.objects.filter(pub_date__date=date)
        return news
    @classmethod
    def search_by_title(cls,search_term):
        news=cls.objects.filter(title__icontains=search_term)
        return news
class NewsLetterRecipients(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
