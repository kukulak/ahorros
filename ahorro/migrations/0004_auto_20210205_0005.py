# Generated by Django 3.1.5 on 2021-02-05 00:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ahorro', '0003_auto_20210205_0002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sistema',
            name='meta',
            field=models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.MinValueValidator(100)]),
        ),
    ]
