# Generated by Django 5.0.3 on 2024-04-14 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tshirts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parentsname', models.CharField(max_length=25)),
                ('membersname', models.CharField(max_length=25)),
                ('color', models.CharField(max_length=25)),
                ('gender', models.CharField(max_length=25)),
                ('size', models.CharField(max_length=25)),
                ('units', models.IntegerField()),
            ],
        ),
    ]