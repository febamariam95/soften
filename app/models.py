from django.db import models

# Create your models here.
class register(models.Model):
    name=models.CharField(max_length=10)
    phone=models.IntegerField()
    email=models.EmailField()
    username=models.CharField(max_length=20,unique=True)
    password=models.CharField(max_length=10)
    def __str__(self):
        return self.username

class product(models.Model):
    product_name=models.CharField(max_length=20)
    price=models.IntegerField()
    stock=models.IntegerField()
    product_image=models.FileField(null=True)

class cart(models.Model):
    product_details=models.ForeignKey(product,on_delete=models.CASCADE)
    user_details=models.ForeignKey(register,on_delete=models.CASCADE)

