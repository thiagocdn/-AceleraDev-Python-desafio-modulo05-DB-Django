# Generated by Django 3.0.6 on 2020-06-11 02:47

import api.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='address',
            field=models.GenericIPAddressField(validators=[django.core.validators.validate_ipv4_address], verbose_name='Endereço IP'),
        ),
        migrations.AlterField(
            model_name='event',
            name='level',
            field=models.CharField(max_length=20, validators=[api.models.level_validator], verbose_name='Nível'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=254, validators=[django.core.validators.EmailValidator], verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(8)], verbose_name='Senha'),
        ),
    ]
