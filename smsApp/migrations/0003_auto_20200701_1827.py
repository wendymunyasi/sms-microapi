# Generated by Django 3.0.7 on 2020-07-01 17:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('smsApp', '0002_message_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='groupID',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
