# Generated by Django 3.0.8 on 2020-07-20 19:47

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('screenshot', cloudinary.models.CloudinaryField(max_length=255, verbose_name='Project screenshot')),
                ('description', models.TextField()),
                ('link', models.URLField()),
                ('post_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'ordering': ['-post_date'],
            },
        ),
    ]
