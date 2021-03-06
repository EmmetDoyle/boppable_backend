# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-10 14:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boppable', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passcode', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('party', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='playlist', to='boppable.Party')),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('track_id', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TrackRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('party', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tracks', to='boppable.Party')),
            ],
        ),
        migrations.CreateModel(
            name='TrackVoting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('votes', models.IntegerField()),
                ('playlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tracks', to='boppable.Playlist')),
                ('track', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boppable.TrackRequest')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.AddField(
            model_name='trackrequest',
            name='suggester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boppable.User'),
        ),
        migrations.AddField(
            model_name='trackrequest',
            name='track',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boppable.Track'),
        ),
        migrations.AddField(
            model_name='party',
            name='host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boppable.User'),
        ),
    ]
