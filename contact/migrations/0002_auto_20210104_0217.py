# Generated by Django 3.1.4 on 2021-01-03 23:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactmessages',
            old_name='date_addes',
            new_name='date_added',
        ),
        migrations.RemoveField(
            model_name='contactmessages',
            name='surname',
        ),
    ]