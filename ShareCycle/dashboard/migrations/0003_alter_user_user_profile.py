# Generated by Django 5.0.6 on 2024-06-15 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_alter_user_user_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_profile',
            field=models.ImageField(blank=True, null=True, upload_to='ShareCycle/static/image'),
        ),
    ]
