# Generated by Django 4.2.5 on 2024-04-26 18:17

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('whispers', '0002_alter_message_related_conversation'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Conversion',
            new_name='Conversation',
        ),
    ]
