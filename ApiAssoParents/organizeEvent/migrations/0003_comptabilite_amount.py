# Generated by Django 4.1.5 on 2023-02-06 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizeEvent', '0002_comptabilite_alter_organisation_password_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comptabilite',
            name='amount',
            field=models.IntegerField(default=50),
            preserve_default=False,
        ),
    ]
