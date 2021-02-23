# Generated by Django 3.1.5 on 2021-02-17 16:38

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ahorro', '0013_auto_20210209_2350'),
    ]

    operations = [
        migrations.CreateModel(
            name='CantidadFija',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('not_archived', models.BooleanField(default=True)),
                ('slug', models.SlugField(blank=True, max_length=200)),
                ('frecuencia', models.CharField(choices=[('1', 'Todos los días'), ('15', 'Cada quince días'), ('30', 'Al mes')], default='30', max_length=200)),
                ('tiempo', models.CharField(choices=[('183', 'Medio año'), ('365', 'Un año'), ('730', 'Dos años'), ('1825', 'Cinco años')], default='365', max_length=200)),
                ('meta', models.IntegerField(validators=[django.core.validators.MinValueValidator(1825, message='Ahorra a partir de 2000')])),
                ('description', models.TextField(blank=True)),
                ('url', models.URLField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='images/%Y/%m/%d/')),
                ('created', models.DateField(auto_now_add=True, db_index=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='systemF_created', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]