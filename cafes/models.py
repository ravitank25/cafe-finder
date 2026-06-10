from django.db import models


class Cafe(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.TextField()

    image = models.ImageField(upload_to="cafes/", blank=True, null=True)

    description = models.TextField(blank=True)

    wifi = models.BooleanField(default=False)
    power_socket = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)

    coffee_price = models.CharField(max_length=20)

    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
