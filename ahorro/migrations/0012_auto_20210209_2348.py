# Generated by Django 3.1.5 on 2021-02-09 23:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ahorro', '0011_auto_20210205_0040'),
    ]

    operations = [
        migrations.AddField(
            model_name='sistema',
            name='archived',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='sistema',
            name='meta',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1825, message='Ahorra a partir de 2000')]),
        ),
    ]