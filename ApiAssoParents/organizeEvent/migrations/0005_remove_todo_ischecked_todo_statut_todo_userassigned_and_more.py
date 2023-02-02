# Generated by Django 4.1.5 on 2023-01-30 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizeEvent', '0004_todo_informations'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='isChecked',
        ),
        migrations.AddField(
            model_name='todo',
            name='statut',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='todo',
            name='userAssigned',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='description',
            field=models.TextField(default='Description par defaut'),
        ),
    ]