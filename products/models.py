from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
    

class Product(models.Model):
    category=models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='products'
    )
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    is_active = models.BooleanField(default= True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
