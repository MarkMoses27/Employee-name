# Generated by Django 4.2.6 on 2023-10-27 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='slug',
            field=models.SlugField(default=''),
        ),
        migrations.AlterField(
            model_name='player',
            name='age',
            field=models.IntegerField(),
        ),
    ]