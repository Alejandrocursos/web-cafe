# Generated by Django 3.1.1 on 2020-12-01 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Services',
            new_name='Service',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='update',
            new_name='updated',
        ),
    ]