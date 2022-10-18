from django.db import models


class Model1(models.Model):
    firstname = models.CharField(max_length=30, help_text="the first name of the professor")
    lastname = models.CharField(max_length=30, help_text="the last name of the professor")
    email = models.EmailField(max_length=50, help_text="the prof mail", null=True)
    promo = models.CharField(max_length=30, help_text="promo", null=True)


class Model2(models.Model):
    module = models.CharField(max_length=40, null=True)
    specialty = models.CharField(max_length=10, null=True)
