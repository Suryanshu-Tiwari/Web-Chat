from django.db import models

# Create your models here.
        
class comment(models.Model):
    name = models.CharField(max_length=30)
    comment = models.TextField()
    isSpam = models.CharField(max_length=10)

    def __str__(self):
        return self.comment
        
class spams(models.Model):
    words = models.CharField(max_length=100)

    def __str__(self):
        return self.words