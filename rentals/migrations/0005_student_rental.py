# Generated by Django 4.1 on 2022-08-30 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0004_student_date_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='rental',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rentals.rental'),
        ),
    ]