# Generated by Django 2.0.13 on 2019-06-17 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0005_remove_listing_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='contact',
            field=models.EmailField(default='email@email.com', max_length=254),
        ),
    ]
