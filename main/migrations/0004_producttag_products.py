# Generated by Django 3.2.11 on 2022-01-22 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_productimage_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='producttag',
            name='products',
            field=models.ManyToManyField(blank=True, to='main.Product'),
        ),
    ]
