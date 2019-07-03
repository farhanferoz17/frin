from django.db import models

# Create your models here.

class Tutorial(models.Model):
    tutorial_title = models.CharField(max_length=200)
    tutorial_content = models.TextField()
    tutorial_published = models.DateTimeField('date published')

    def __str__(self):
        return self.tutorial_title

class User(models.Model):
    user_name = models.CharField(max_length=200)
    user_id = models.PositiveIntegerField()
    user_desc = models.TextField()
    user_email = models.CharField(max_length=200)
    user_pass = models.CharField(max_length=200)
    user_bd = models.DateTimeField('date published')

    def __str__(self):
        return self.user_name
