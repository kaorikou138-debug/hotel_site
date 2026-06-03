from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name


class DailyPrice(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    date = models.DateField()
    price = models.IntegerField()

    def __str__(self):
        return f"{self.hotel.name} - {self.date} - {self.price}円"