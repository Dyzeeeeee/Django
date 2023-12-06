from django.db import models

# Create your models here.

class Menu(models.Model):
    category = models.TextField()
    subcategory = models.TextField() 
    item = models.TextField()
    description = models.TextField()
    image = models.TextField()
    price = models.TextField()

    class Meta:
        managed = False
        db_table = 'menu'