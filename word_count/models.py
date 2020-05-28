from django.db import models


class Word(models.Model):
    word = models.CharField()
    count = models.IntegerField(min_value=1)
    file_name = models.CharField(null=False, blank=False)
    sentence = models.JSONField()

    def __str__(self):
        return self.word
