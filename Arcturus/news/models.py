from django.db import models

class New(models.Model):
    title = models.CharField(max_length=500)
    date = models.DateField()
    text = models.TextField()
    id_field = models.IntegerField(verbose_name="id")

    def __str__(self):
        return self.title