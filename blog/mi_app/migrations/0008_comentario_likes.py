# Generated by Django 5.1 on 2024-08-24 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mi_app', '0007_comentario'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
