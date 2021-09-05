# Generated by Django 3.1.5 on 2021-09-04 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('publishers', '0001_initial'),
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='publisher',
            field=models.ManyToManyField(to='publishers.Publisher'),
        ),
    ]