# Generated by Django 2.1.2 on 2018-10-16 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rss_agregator', '0002_auto_20181016_0135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created',
            field=models.CharField(max_length=100, verbose_name='Published'),
        ),
    ]