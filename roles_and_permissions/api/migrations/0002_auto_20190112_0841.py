# Generated by Django 2.1.5 on 2019-01-12 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='permission',
            old_name='permission',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='role',
            old_name='role',
            new_name='name',
        ),
    ]
