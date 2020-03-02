from django.db import models

# Create your models here.
class Vocabulary(models.Model):

    korean = models.CharField(max_length=200)
    english = models.CharField(max_length=200)
    spanish = models.CharField(max_length=200, null=False)
    category = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.spanish

