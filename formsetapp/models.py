from django.db import models

# Create your models here.
class Customer(models.Model):
	cust_id = models.AutoField(primary_key=True)
	cust_name = models.CharField(max_length=30)
	cust_addr = models.CharField(max_length=30)
	cust_no = models.CharField(max_length=10)
	def __str__(self):
		return self.cust_name

class Order(models.Model):
	order_id = models.AutoField(primary_key=True)
	cust_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
	order_menu = models.CharField(max_length=20)
	order_quantity = models.CharField(max_length=3)
	order_price = models.CharField(max_length=5)