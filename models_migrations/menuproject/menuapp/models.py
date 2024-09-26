from django.db import models
from unicodedata import name

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    price = models.IntegerField()
    
    def __str__(self):
        return self.name + " : " + self.cuisine
    
    
class Menuitems(models.Model):
    itemname = models.CharField(max_length=200)
    category = models.CharField(max_length=300)
    year= models.IntegerField()
    
    def __str__(self):
        return self.name + " : " + self.course + " : " + str(self.year)
    
    
class Drinks(models.Model):
    drink_name=models.CharField(max_length= 200)
    price = models.IntegerField()
    
    def __str__(self):
        return self.drink + " : " + str(self.price)
    
    
class MenuCategory(models.Model):
    menu_category_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.menu_category_name
    
class Menus(models.Model):
    menu_item = models.CharField(max_length=200)
    price = models.IntegerField(null=False)
    category_id = models.ForeignKey(MenuCategory, on_delete=models.PROTECT, default = None, related_name = "category_name")
    
    def __str__(self):
        return self.menu_item + " : " + str(self.price) + " : " + str(self.category_id)


class Customer(models.Model):
    name= models.CharField(max_length=200)
    reservation_day= models.CharField(max_length=200)
    seats  = models.IntegerField()
    
    def __str__(self):
        return self.name