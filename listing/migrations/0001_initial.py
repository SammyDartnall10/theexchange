# Generated by Django 2.2.3 on 2019-07-18 20:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ListingArchive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Listing Title', max_length=254)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='images')),
                ('contact', models.EmailField(default='email@email.com', max_length=254)),
                ('tag', models.TextField()),
                ('can_offer', models.TextField(default=1)),
                ('created_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='listings', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='Listing Title', max_length=254)),
                ('content', models.TextField(verbose_name='What are you looking for? Be as detailed as possible!')),
                ('image', models.ImageField(upload_to='images')),
                ('contact', models.EmailField(default='The best email for people to contact you at', max_length=254)),
                ('tag', models.TextField()),
                ('can_offer', models.TextField(default='Please detail the things you can offer in return as single words, eg catering, photography')),
                ('archive', models.BooleanField()),
                ('created_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
