# Generated by Django 5.0.6 on 2024-06-15 16:46

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_alter_user_user_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='item_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
