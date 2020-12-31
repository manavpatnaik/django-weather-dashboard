from django.db import models

class City(models.Model):
    city_name = models.CharField(max_length=50)
    date_searched = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.city_name

