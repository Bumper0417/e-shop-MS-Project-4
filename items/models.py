from django.db import models

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=240, default='')
    introduction = models.TextField()
    features = models.TextField()
    description = models.TextField()
    code = models.DecimalField(max_digits=6, decimal_places=2)
    availability = models.DecimalField(max_digits=3, decimal_places=0)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name

