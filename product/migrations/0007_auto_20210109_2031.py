# Generated by Django 3.1.4 on 2021-01-09 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20210109_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]