from django.db import models


class Post(models.Model):
    title = model.CharField()
    date = models.DateField()
    content = models.TextField()
