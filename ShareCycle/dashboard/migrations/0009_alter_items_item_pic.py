# Generated by Django 5.0.6 on 2024-06-16 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_remove_items_item_id_alter_items_item_pic_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='item_pic',
            field=models.ImageField(blank=True, null=True, upload_to='static/images'),
        ),
    ]
