# Generated by Django 4.1.7 on 2023-05-05 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfer',
            name='transfertime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
