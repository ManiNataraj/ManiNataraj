# Generated by Django 5.1.2 on 2024-11-29 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0009_advertisement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(choices=[('home', 'Home'), ('world', 'World'), ('politics', 'Politics'), ('sports', 'Sports'), ('entertainment', 'Entertainment'), ('innovations', 'Innovations'), ('bussiness', 'Bussiness')], default='home', max_length=20),
        ),
    ]