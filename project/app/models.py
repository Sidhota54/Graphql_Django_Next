from multiprocessing.sharedctypes import Value
from django.db import models



class Store(models.Model):
    store_name = models.CharField(max_length = 100)
    store_url = models.URLField(max_length=200)
    store_logo = models.ImageField(upload_to = "images")
    admin_mail = models.CharField(max_length = 100)
    # default = models.BooleanField()
    
    def __str__(self):
        return self.store_name
    
class Columns(models.Model):
    name = models.CharField(max_length = 100)
    value = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
        
class Products(models.Model):
    column_id = models.ForeignKey(Columns, on_delete=models.CASCADE)
    
    def saveColumns(self):
        self.save()
        
    def get_products_by_column(column_id):
        return Products.objects.filter(columns = column_id)
    
class Store_products(models.Model):
    store_id = models.ForeignKey(Store, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    
class Orders(models.Model):
    column_id = models.ForeignKey(Columns, on_delete=models.CASCADE)
    
class store_orders(models.Model):
    store_id = models.ForeignKey(Store,on_delete=models.CASCADE)
    orders_id = models.ForeignKey(Orders, on_delete=models.CASCADE)    
    