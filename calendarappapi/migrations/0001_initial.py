# Generated by Django 4.1.2 on 2022-10-20 03:47

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
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date_start', models.DateField()),
                ('date_end', models.DateField(blank=True)),
                ('time_start', models.TimeField()),
                ('time_end', models.TimeField(blank=True)),
                ('cost', models.CharField(max_length=100)),
                ('about', models.CharField(blank=True, max_length=1000)),
                ('street', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=15)),
                ('zip', models.IntegerField()),
                ('social_one', models.CharField(blank=True, max_length=25)),
                ('social_two', models.CharField(blank=True, max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('abbreviation', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.CharField(max_length=10000)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calendarappapi.event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calendarappapi.state'),
        ),
        migrations.AddField(
            model_name='event',
            name='tags',
            field=models.ManyToManyField(related_name='events', to='calendarappapi.tag'),
        ),
        migrations.AddField(
            model_name='event',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1000)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calendarappapi.event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
