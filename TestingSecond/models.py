from django.db import models

class Item(models.Model):
    item_name = models.CharField(max_length=30)