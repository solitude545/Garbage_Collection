# Generated by Django 5.1.1 on 2024-10-01 15:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customers', '0003_alter_user_reg_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=128)),
            ],
        ),
        migrations.RemoveField(
            model_name='user_reg',
            name='password',
        ),
        migrations.RemoveField(
            model_name='user_reg',
            name='username',
        ),
        migrations.AddField(
            model_name='user_reg',
            name='login',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='Customers.login'),
        ),
    ]
