# Generated by Django 5.0.3 on 2024-04-14 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chessapp', '0005_events'),
    ]

    operations = [
        migrations.RenameField(
            model_name='events',
            old_name='membersname',
            new_name='membersname1',
        ),
        migrations.RenameField(
            model_name='events',
            old_name='parentsname',
            new_name='parentsname1',
        ),
        migrations.AlterField(
            model_name='events',
            name='Class',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='events',
            name='dob',
            field=models.CharField(max_length=25),
        ),
    ]
