from django.db import models
from django.contrib.auth.hashers import check_password



class user_reg(models.Model):
    username = models.CharField(max_length=100, unique=True, default='default_username') 
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=100)
    
    # Add any other fields or methods if needed


    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
