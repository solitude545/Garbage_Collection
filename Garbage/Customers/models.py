from django.db import models

from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import AbstractUser , Group, Permission
from django.utils.translation import gettext_lazy as _

class User(AbstractUser ):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        related_name="custom_user_set",
        related_query_name="custom_user",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name="custom_user_permissions",
    )

class UserProfile(models.Model):
    user = models.OneToOneField('Customers.User', on_delete=models.CASCADE, null=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.user.username