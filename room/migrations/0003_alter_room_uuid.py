# Generated by Django 3.2.13 on 2022-07-03 06:22

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0002_alter_room_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('b9454599-8621-4310-8821-8a533b37ef72')),
        ),
    ]
