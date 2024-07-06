from django.db import models

class Studentdb(models.Model):
    name = models.CharField(max_length=25)
    age = models.IntegerField(default=1)
    email = models.EmailField()
    phone = models.BigIntegerField(default=123)
    address = models.CharField(max_length=70)

    def __str__(self):
        return self.name
