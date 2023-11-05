# Generated by Django 4.2.7 on 2023-11-05 02:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_doctor'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='primary_doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.doctor'),
        ),
    ]
