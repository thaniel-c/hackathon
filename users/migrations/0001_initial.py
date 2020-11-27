# Generated by Django 2.2.12 on 2020-06-14 09:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MasterControl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allowing_new_users', models.BooleanField(default=True)),
                ('allowing_viewing_submissions', models.BooleanField(default=False)),
                ('allow_submissions', models.BooleanField(default=True)),
                ('allow_viewing_winners', models.BooleanField(default=False)),
                ('allow_voting', models.BooleanField(default=False)),
                ('timer_date', models.TextField(default='January 1, 2030 00:00:00')),
                ('timer_message', models.TextField(default='Event starts on January 1st, 2030!')),
                ('youtube_embed_code', models.TextField(default='S7SLep244ss')),
                ('identifier', models.TextField(default='MASTER', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Submission', max_length=100)),
                ('content', models.TextField(default='Nothing has been written about this submission yet....')),
                ('date', models.DateTimeField(auto_now=True)),
                ('Main_Link', models.CharField(default='https://www.google.com/', max_length=100)),
                ('label_Main_Link', models.CharField(default='Main', max_length=26)),
                ('Link2', models.CharField(blank=True, default='', max_length=100)),
                ('label_Link2', models.CharField(blank=True, default='Link 2', max_length=26)),
                ('Link3', models.CharField(blank=True, default='', max_length=100)),
                ('label_Link3', models.CharField(blank=True, default='Link 3', max_length=26)),
                ('Link4', models.CharField(blank=True, default='', max_length=100)),
                ('label_Link4', models.CharField(blank=True, default='Link 4', max_length=26)),
                ('imagelink', models.CharField(blank=True, default='', max_length=100)),
                ('Score', models.IntegerField(default=0)),
                ('actualSubmission', models.BooleanField(default=False)),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CHOICES', models.ManyToManyField(blank=True, to='users.Submission')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=100)),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='submission',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Team'),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('bio', models.TextField(default='Nothing has been written here yet...', null=True)),
                ('hasVoted', models.BooleanField(default=False)),
                ('submission', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Submission')),
                ('team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Team')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
