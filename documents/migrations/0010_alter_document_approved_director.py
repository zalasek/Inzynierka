# Generated by Django 3.2.8 on 2021-11-18 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0009_alter_assignment_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='approved_director',
            field=models.BooleanField(blank=True, choices=[(False, 'No'), (True, 'Yes')], default=False, null=True),
        ),
    ]
