# Generated by Django 4.1.3 on 2023-04-20 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='store',
            old_name='address',
            new_name='certificate',
        ),
    ]