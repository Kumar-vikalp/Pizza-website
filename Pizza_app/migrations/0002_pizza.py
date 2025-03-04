# Generated by Django 4.2.16 on 2024-10-14 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pizza_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('type', models.CharField(max_length=20)),
                ('size', models.CharField(max_length=10)),
                ('image_url', models.URLField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='pizzas/')),
            ],
        ),
    ]
