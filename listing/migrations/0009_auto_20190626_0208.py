# Generated by Django 2.2.2 on 2019-06-26 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0008_auto_20190617_2025'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='can_offer',
            field=models.TextField(default=1),
        ),
        migrations.AlterField(
            model_name='listing',
            name='title',
            field=models.CharField(default='Listing Title', max_length=254),
        ),
    ]