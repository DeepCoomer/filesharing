# Generated by Django 4.2.2 on 2023-06-18 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='files',
            name='created_at',
            field=models.DateField(auto_now=True),
        ),
    ]
