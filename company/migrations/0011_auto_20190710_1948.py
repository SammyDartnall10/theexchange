# Generated by Django 2.2.2 on 2019-07-10 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0010_companyreview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companydetail',
            name='industry',
            field=models.CharField(blank=True, choices=[('AG', 'Agriculture, forestry, fishing and hunting'), ('CN', 'Construction'), ('MG', 'Manufacturing'), ('TR', 'Transportation equipment manufacturing'), ('SI', 'Service industries'), ('WT', 'Wholesale Trade'), ('RT', 'Retail Trade'), ('TW', 'Transportation and warehousing'), ('IC', 'Information and cultural industries'), ('FI', 'Finance and insurance'), ('RE', 'Real estate and rental and leasing'), ('PS', 'Professional, scientific, and technical services'), ('MA', 'Management of companies and enterprises'), ('AD', 'Administrative and support, waste management and remediation services')], default='Please pick an industry', max_length=254, null=True),
        ),
    ]