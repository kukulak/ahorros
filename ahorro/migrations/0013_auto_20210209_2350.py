# Generated by Django 3.1.5 on 2021-02-09 23:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ahorro', '0012_auto_20210209_2348'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sistema',
            old_name='archived',
            new_name='not_archived',
        ),
    ]
