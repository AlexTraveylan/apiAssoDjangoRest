# Generated by Django 4.1.5 on 2023-01-30 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizeEvent', '0005_remove_todo_ischecked_todo_statut_todo_userassigned_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='userAssigned',
            field=models.TextField(null=True),
        ),
    ]
