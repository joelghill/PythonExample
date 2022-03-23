from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=5)
    last_name = models.CharField(max_length=5)
    age = models.IntegerField(null=True)
    birthday = models.DateField(null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Pet(models.Model):
    name = models.CharField(max_length=150)
    species = models.CharField(max_length=150)
    owner = models.ForeignKey(Person, on_delete=models.SET_NULL, related_name="pets", null=True)