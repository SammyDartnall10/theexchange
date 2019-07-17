# Generated by Django 2.2.2 on 2019-06-26 17:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0002_companydetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='companydetail',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='companydetail',
            name='about_us',
            field=models.CharField(default="Information about your company - where you're from, what you do!", max_length=254),
        ),
        migrations.AlterField(
            model_name='companydetail',
            name='contact_email',
            field=models.EmailField(default='contact email', max_length=254),
        ),
        migrations.AlterField(
            model_name='companydetail',
            name='industry',
            field=models.CharField(choices=[('Agriculture, forestry, fishing and hunting', 'Agriculture, forestry, fishing and hunting'), ('Construction', 'Construction'), ('Manufacturing', 'Manufacturing'), ('Transportation equipment manufacturing', 'Transportation equipment manufacturing'), ('Service industries', 'Service industries'), ('Wholesale Trade', 'Wholesale Trade'), ('Retail Trade', 'Retail Trade'), ('Transportation and warehousing', 'Transportation and warehousing'), ('Information and cultural industries', 'Information and cultural industries'), ('Finance and insurance', 'Finance and insurance'), ('Real estate and rental and leasing', 'Real estate and rental and leasing'), ('Professional, scientific, and technical services', 'Professional, scientific, and technical services'), ('Management of companies and enterprises', 'Management of companies and enterprises'), ('Administrative and support, waste management and remediation services', 'Administrative and support, waste management and remediation services'), ('Mining, quarrying, and oil and gas extraction', 'Mining, quarrying, and oil and gas extraction')], default='Industry', max_length=1),
        ),
    ]