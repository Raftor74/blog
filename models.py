from django.db import models

# Create your models here.


class News (models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    time = models.DateTimeField()

    def __str__(self):
        return self.title