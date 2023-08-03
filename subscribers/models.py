from django.db import models

# Create your models here.
class Subscriber(models.Model):
    email = models.CharField(max_length=200, null=False, blank=False)
    full_name = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.email