# Generated by Django 3.2.4 on 2021-08-18 07:23

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz', '0003_patternstatistics'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='leitnerbox',
            unique_together={('user', 'pattern', 'box_number')},
        ),
    ]