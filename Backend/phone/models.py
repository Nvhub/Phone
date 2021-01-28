from django.db import models



class Persons(models.Model): 

    name = models.CharField(max_length = 30)
    phone_number = models.CharField(max_length = 12)
    email = models.EmailField(null = True)
    rel = models.CharField(max_length = 30)