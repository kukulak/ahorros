# Generated by Django 3.1.5 on 2021-02-18 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ahorro', '0017_ahorro_sistemaf'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ahorro',
            name='sistemaF',
        ),
    ]