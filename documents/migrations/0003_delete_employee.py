# Generated by Django 3.2.8 on 2021-10-24 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0002_employee'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Employee',
        ),
    ]