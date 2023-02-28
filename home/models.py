from django.db import models


class Message(models.Model):
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

