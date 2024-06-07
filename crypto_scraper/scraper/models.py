from django.db import models


class ScrapingTask(models.Model):
    coin = models.CharField(max_length=100)
    output = models.JSONField(null=True, blank=True)
    error = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.coin