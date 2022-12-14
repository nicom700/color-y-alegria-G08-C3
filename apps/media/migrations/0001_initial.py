# Generated by Django 4.0.8 on 2022-12-19 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('posts', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, default=None, null=True, upload_to='posts')),
                ('is_first', models.BooleanField(default=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.posts')),
            ],
            options={
                'db_table': 'media',
                'managed': True,
            },
        ),
    ]
