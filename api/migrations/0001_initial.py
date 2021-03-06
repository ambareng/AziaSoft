# Generated by Django 3.1.7 on 2021-03-29 11:24

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DriversEducation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=255)),
                ('modified_by', models.CharField(max_length=255)),
                ('modified_date', models.DateField(verbose_name=django.utils.timezone.now)),
                ('is_active', models.BooleanField(default=True)),
                ('school', models.CharField(max_length=255)),
                ('instructor', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MedicalType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=255)),
                ('modified_by', models.CharField(max_length=255)),
                ('modified_date', models.DateField(verbose_name=django.utils.timezone.now)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MedicalProvider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=255)),
                ('modified_by', models.CharField(max_length=255)),
                ('modified_date', models.DateField(verbose_name=django.utils.timezone.now)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('address', models.CharField(max_length=255)),
                ('contact_no', models.CharField(max_length=255)),
                ('contact_person', models.CharField(max_length=255)),
                ('contact_person_address', models.CharField(max_length=255)),
                ('contact_person_phone_number', models.CharField(max_length=255)),
                ('medical_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.medicaltype')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
