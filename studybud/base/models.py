from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    number = models.CharField(max_length=10)
    date = models.DateField()

    # Replace the object(1) to the user name in DB
    def __str__(self) -> str:
        return self.name
