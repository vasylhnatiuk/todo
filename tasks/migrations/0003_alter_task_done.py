# Generated by Django 4.0.6 on 2022-07-11 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_alter_task_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='done',
            field=models.BooleanField(blank=None, null=True),
        ),
    ]
