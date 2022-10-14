from django.db import models

# Create your models here.

class User(models.Model):
    type_user = (('C', 'Customer'), ('E', 'Employee'))
    user_ID = models.AutoField(primary_key=True)
    username = models.CharField(max_length=15, unique = True)
    password = models.CharField(max_length=15)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    type = models.CharField(max_length=1, choices=type_user)

    def __str__(self):
        return self.username

class Employee(User):
    address = models.CharField(max_length=50)
    mobileNumber = models.CharField(max_length=13)


class Customer(User):
    age = models.IntegerField()

class Supplier(models.Model):
    supplier_ID = models.AutoField(primary_key=True)
    companyName = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=50)
    mobileNumber = models.CharField(max_length=13)

    def __str__(self):
        return self.companyName


class Product(models.Model):
    product_ID = models.AutoField(primary_key=True)
    prodName = models.CharField(max_length=50, unique=True)
    prodQty = models.IntegerField()
    prodPrice = models.IntegerField()
    supplier_ID = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    def __str__(self):
        return self.prodName

class Sales(models.Model):
    salesID = models.AutoField(primary_key=True)
    cUser_ID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    eUser_ID = models.ForeignKey(Employee, on_delete=models.CASCADE)
    product_ID = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    dateOfSale = models.DateField()
