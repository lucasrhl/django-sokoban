from django.db import models


class Map(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True, default='')
    content = models.CharField(max_length=1024, null=True, blank=True, default='')

    def __str__(self):
        return self.title
