from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=35)
    text = models.CharField(max_length=255)
    author = models.CharField(max_length=60)

