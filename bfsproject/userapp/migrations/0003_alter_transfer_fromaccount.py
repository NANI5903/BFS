# Generated by Django 4.1.7 on 2023-05-05 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0002_alter_transfer_transfertime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfer',
            name='fromaccount',
            field=models.CharField(max_length=255),
        ),
    ]