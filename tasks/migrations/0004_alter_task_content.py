# Generated by Django 4.0.6 on 2022-07-11 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_alter_task_done'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='content',
            field=models.CharField(max_length=255),
        ),
    ]
