# Generated by Django 4.1 on 2022-08-30 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('reg_number', models.CharField(max_length=255, unique=True)),
                ('id_number', models.CharField(max_length=25)),
                ('gender', models.CharField(choices=[('female', 'Female'), ('male', 'Male')], max_length=255)),
                ('room_number', models.CharField(max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], max_length=255)),
            ],
        ),
    ]