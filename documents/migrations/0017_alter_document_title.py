# Generated by Django 3.2.8 on 2021-12-30 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0016_alter_document_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='title',
            field=models.CharField(default='', max_length=250),
        ),
    ]
