# Generated by Django 3.2.8 on 2021-11-18 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0011_alter_document_approved_pm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='status',
            field=models.CharField(blank=True, choices=[('Assigned to director', 'Assigned to director'), ('Waiting', 'Waiting for checks'), ('Checked', 'Checked'), ('Approved', 'Approved'), ('Waiting for payment', 'Waiting for payment'), ('Paid', 'Paid')], max_length=50, null=True),
        ),
    ]
