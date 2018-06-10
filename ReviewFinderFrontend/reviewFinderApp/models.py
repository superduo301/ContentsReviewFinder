from django.db import models


# Create your models here.

class Channel(models.Model):
    type = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    url = models.URLField()
    etag = models.CharField(max_length=200)
    last_modified = models.DateTimeField()

    def __str__(self):
        return super().__str__()


