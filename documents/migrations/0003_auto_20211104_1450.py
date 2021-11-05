# Generated by Django 3.2.8 on 2021-11-04 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_auto_20211104_1447'),
        ('documents', '0002_auto_20211104_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='document',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='documents.document'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='employees.employee'),
        ),
    ]