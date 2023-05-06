# Generated by Django 4.1.7 on 2023-05-05 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'admin_table',
            },
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('fullname', models.CharField(max_length=100)),
                ('fathername', models.CharField(max_length=100)),
                ('mothername', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('Others', 'Prefer not to say')], max_length=10)),
                ('dateofbirth', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('contactno', models.BigIntegerField(unique=True)),
                ('panno', models.BigIntegerField(unique=True)),
                ('aadharno', models.CharField(max_length=100)),
                ('registrationtime', models.DateTimeField(auto_now=True)),
                ('address', models.CharField(max_length=100, unique=True)),
                ('amount', models.IntegerField(default=1000)),
                ('customer_image', models.FileField(upload_to='customerimages/')),
                ('credit_score', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'registration_table',
            },
        ),
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('transaction_id', models.AutoField(primary_key=True, serialize=False)),
                ('fromaccount', models.TextField(max_length=255)),
                ('amount', models.IntegerField()),
                ('purpose', models.CharField(max_length=100)),
                ('transfertime', models.DateTimeField(default='2023-05-05 14:30:32.243125')),
                ('toaccount', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.registration')),
            ],
            options={
                'db_table': 'transfer_table',
            },
        ),
        migrations.CreateModel(
            name='BillPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_type', models.CharField(choices=[('E', 'Electricity'), ('W', 'Water'), ('G', 'Gas')], max_length=20)),
                ('bill_number', models.CharField(max_length=50)),
                ('amount', models.IntegerField()),
                ('payment_time', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.registration')),
            ],
            options={
                'db_table': 'billpayment_table',
            },
        ),
    ]
