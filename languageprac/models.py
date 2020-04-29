from django.db import models

# Create your models here.
from django.utils import timezone

from polls.models import User


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


class Record(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    eng = models.CharField(max_length=300)
    kor = models.CharField(max_length=300)
    esp = models.CharField(max_length=300)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    modified_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.eng


class FavouriteVocabulary(models.Model):
    category_vocab = models.ForeignKey(Vocabulary, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class FavouriteRecord(models.Model):
    record = models.ForeignKey(Record, on_delete=models.CASCADE, null=True)


class Favourite(models.Model):
    type = models.IntegerField(null=False)
    type_id = models.IntegerField(null=False)