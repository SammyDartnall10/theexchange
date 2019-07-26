# Generated by Django 2.2.3 on 2019-07-25 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_auto_20190725_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companydetail',
            name='industry',
            field=models.CharField(blank=True, choices=[('Agriculture, forestry, fishing and hunting', 'Agriculture, forestry, fishing and hunting'), ('Construction', 'Construction'), ('Manufacturing', 'Manufacturing'), ('Transportation equipment manufacturing', 'Transportation equipment manufacturing'), ('Service industries', 'Service industries'), ('Wholesale Trade', 'Wholesale Trade'), ('Retail Trade', 'Retail Trade'), ('Transportation and warehousing', 'Transportation and warehousing'), ('Information and cultural industries', 'Information and cultural industries'), ('Finance and insurance', 'Finance and insurance'), ('Real estate and rental and leasing', 'Real estate and rental and leasing'), ('Professional, scientific, and technical services', 'Professional, scientific, and technical services'), ('Management of companies and enterprises', 'Management of companies and enterprises'), ('Administrative and support, waste management and remediation services', 'Administrative and support, waste management and remediation services')], default='Please pick an industry', max_length=254, null=True),
        ),
    ]