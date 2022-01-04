# Generated by Django 3.2.8 on 2022-01-04 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0018_alter_document_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='status',
            field=models.CharField(blank=True, choices=[('Assigned to director', 'Waiting for assignment to PM'), ('Waiting', 'Waiting for checks'), ('Checked', 'Waiting for director to approve'), ('Waiting for payment', 'Waiting for payment'), ('Paid', 'Paid')], max_length=50, null=True),
        ),
    ]
