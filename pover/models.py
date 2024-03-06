from django.db import models

# Create your models here.
class Link(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField(max_length=200)

    def __str__(self):
        return [self.name, self.url]