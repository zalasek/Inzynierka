# Generated by Django 3.2.8 on 2021-10-28 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0011_auto_20211028_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='document',
            field=models.ManyToManyField(to='documents.Document'),
        ),
    ]