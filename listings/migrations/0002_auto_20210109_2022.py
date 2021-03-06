# Generated by Django 3.1.5 on 2021-01-09 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rent',
            name='slug',
            field=models.SlugField(default=1, max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sale',
            name='slug',
            field=models.SlugField(default=1, max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rent',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='sale',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
