# Generated by Django 3.1.4 on 2021-01-03 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='detail_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
