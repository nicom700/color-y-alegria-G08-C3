# Generated by Django 4.0.8 on 2022-12-13 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='photo',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
    ]
