# Generated by Django 3.2.8 on 2021-10-28 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
        ('documents', '0014_auto_20211028_1709'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='assigned',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employees.employee'),
        ),
    ]
