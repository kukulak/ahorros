# Generated by Django 3.1.5 on 2021-02-22 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ahorro', '0021_auto_20210222_1824'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ahorrareslameta',
            name='cantidad',
        ),
    ]
