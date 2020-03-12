from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published', auto_now_add=True)

    def __str__(self):
        return self.name

class Vocabulary(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    kor = models.CharField(max_length=200)
    eng = models.CharField(max_length=200)
    esp = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    def __str__(self):
        return self.eng

