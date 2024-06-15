from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_profile = models.ImageField(upload_to="ShareCycle/static/image", blank=True, null=True)
    user_contact = models.PositiveBigIntegerField()
    user_address = models.CharField(max_length=30)

class Items(models.Model):
    category = [
        ('Food', 'Food'),
        ('Clothing', 'Clothing'),
        ('Electronics', 'Electronics'),
        ('Books', 'Books'),
        ('Other', 'Other')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=20)
    
    item_exp_date = models.DateField()
    item_collect_before = models.DateField()
    item_description = models.CharField(max_length=50)
    item_category = models.CharField(choices=category, max_length=15)

    def __str__(self):
        return self.item_name