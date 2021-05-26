from django.db import models
from django_countries.fields import CountryField

class Destination(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
    from_city = models.CharField(max_length=200, null=True, blank=True )
    destination = models.CharField(max_length=200, null=True, blank=True)
    country = CountryField(null=True, blank=True)
    departure = models.DateTimeField(null=True, blank=True)
    total_days = models.IntegerField( null=True, blank=True)
