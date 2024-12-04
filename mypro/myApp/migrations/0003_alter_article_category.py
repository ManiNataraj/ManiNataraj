# Generated by Django 5.1.2 on 2024-10-27 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0002_article_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(choices=[('home', 'Home'), ('world', 'World'), ('politics', 'Politics'), ('sports', 'Sports'), ('entertainment', 'Entertainment')], default='home', max_length=20),
        ),
    ]