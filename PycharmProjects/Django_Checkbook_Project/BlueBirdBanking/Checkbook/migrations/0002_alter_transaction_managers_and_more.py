# Generated by Django 5.0.7 on 2024-07-26 22:58

import django.db.models.manager
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Checkbook', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='transaction',
            managers=[
                ('Transactions', django.db.models.manager.Manager()),
            ],
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='data',
            new_name='date',
        ),
    ]
