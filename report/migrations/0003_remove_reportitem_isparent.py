# Generated by Django 3.2.4 on 2021-10-25 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0002_auto_20211025_1316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reportitem',
            name='isParent',
        ),
    ]