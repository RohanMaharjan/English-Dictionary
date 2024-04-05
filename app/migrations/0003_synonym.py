# Generated by Django 5.0.3 on 2024-03-22 12:23

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_meaning_word'),
    ]

    operations = [
        migrations.CreateModel(
            name='Synonym',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('synonym', models.TextField()),
                ('word', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='synonym', to='app.word')),
            ],
        ),
    ]