# Generated by Django 3.1.5 on 2021-08-23 16:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ahorro', '0024_auto_20210802_1717'),
    ]

    operations = [
        migrations.AddField(
            model_name='sistema',
            name='email',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='sistema',
            name='push',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='ahorro',
            name='cantidad',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1, message='Vamos, a que puedes ahorrar más de 10 pesos')]),
        ),
    ]
