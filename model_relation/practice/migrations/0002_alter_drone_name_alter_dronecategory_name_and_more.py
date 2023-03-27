# Generated by Django 4.0 on 2023-03-26 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drone',
            name='name',
            field=models.CharField(max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='dronecategory',
            name='name',
            field=models.CharField(max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='pilot',
            name='name',
            field=models.CharField(default='', max_length=250, unique=True),
        ),
    ]
