# Generated by Django 5.0.6 on 2024-06-15 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_contact',
            field=models.PositiveBigIntegerField(),
        ),
    ]