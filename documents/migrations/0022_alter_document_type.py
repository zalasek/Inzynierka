# Generated by Django 3.2.8 on 2022-01-09 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0021_auto_20220106_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='type',
            field=models.CharField(choices=[('product', 'Product'), ('service', 'Service')], default='', max_length=30),
        ),
    ]
