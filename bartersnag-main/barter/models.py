from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'
        
    def __str__(self):
        return self.name
    
class Location(models.Model):
    location = models.CharField(max_length=255)
    
    class Meta:
        ordering = ('location',)
        
    def __str__(self):
        return self.location
    
class Barter(models.Model):
    category = models.ForeignKey(Category, related_name='barters', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    #exchange_item = models.CharField(max_length=255)
    exchange_item = models.ForeignKey('self', related_name='related_barters', on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='barter_images', blank=True, null=True)
    is_exchanged = models.BooleanField(default=False)
    location = models.ForeignKey(Location, related_name='locations', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='barters', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name