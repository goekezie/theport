# Generated by Django 3.1.6 on 2021-02-21 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theportapp', '0002_remove_comment_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='project',
        ),
    ]
