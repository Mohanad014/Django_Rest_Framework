from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.category_name

class Product(models.Model):

    category_reference = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    p_name = models.CharField(max_length=200, null=True)
    code = models.CharField(max_length=200, null=True)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.p_name
    
