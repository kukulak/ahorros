# Generated by Django 3.1.5 on 2021-02-05 00:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ahorro', '0010_auto_20210205_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sistema',
            name='meta',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(100)]),
        ),
    ]