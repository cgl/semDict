from django.db import models
from django.utils import timezone


class Group(models.Model):
    name = models.CharField(max_length=200)
    description =  models.TextField()
    
class Token(models.Model):
    #author = models.ForeignKey('auth.User')
    group = models.ForeignKey(Group)
    lemma = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.lemma
