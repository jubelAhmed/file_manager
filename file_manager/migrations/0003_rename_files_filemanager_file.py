# Generated by Django 3.2.9 on 2021-11-26 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('file_manager', '0002_alter_filemanager_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='filemanager',
            old_name='files',
            new_name='file',
        ),
    ]
