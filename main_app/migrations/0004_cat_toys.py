# Generated by Django 3.1.2 on 2020-10-08 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20201008_1011'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat',
            name='toys',
            field=models.ManyToManyField(to='main_app.Toy'),
        ),
    ]