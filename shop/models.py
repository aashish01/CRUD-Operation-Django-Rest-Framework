from django.db import models

# Create your models here.
class item(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.FloatField()
    brand = models.CharField(max_length=40)

    class meta:
        db_table='item'