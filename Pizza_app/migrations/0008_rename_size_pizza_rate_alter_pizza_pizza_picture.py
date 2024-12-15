# Generated by Django 4.2.16 on 2024-12-13 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pizza_app', '0007_rename_profile_picture_pizza_pizza_picture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pizza',
            old_name='size',
            new_name='rate',
        ),
        migrations.AlterField(
            model_name='pizza',
            name='pizza_picture',
            field=models.ImageField(blank=True, null=True, upload_to='pizza_pics/'),
        ),
    ]
