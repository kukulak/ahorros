# Generated by Django 3.1.5 on 2021-02-22 22:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ahorro', '0022_remove_ahorrareslameta_cantidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ahorro',
            name='cantidad',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(10, message='Vamos, a que puedes ahorrar mas de 10 pesos')]),
        ),
    ]
