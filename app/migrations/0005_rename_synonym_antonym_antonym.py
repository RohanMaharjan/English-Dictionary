# Generated by Django 5.0.3 on 2024-03-27 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_antonym'),
    ]

    operations = [
        migrations.RenameField(
            model_name='antonym',
            old_name='synonym',
            new_name='antonym',
        ),
    ]