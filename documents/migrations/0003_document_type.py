# Generated by Django 3.2.8 on 2021-11-02 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0002_auto_20211102_1135'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='type',
            field=models.CharField(blank=True, choices=[('product', 'Product'), ('service', 'Service')], max_length=30, null=True),
        ),
    ]
