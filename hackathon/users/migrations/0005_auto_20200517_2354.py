# Generated by Django 3.0.5 on 2020-05-18 03:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='team',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.Team'),
        ),
    ]