# Generated by Django 3.2.8 on 2021-11-01 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0005_remove_todo_off_listed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('note_id', models.AutoField(primary_key=True, serialize=False)),
                ('note_text', models.CharField(max_length=444)),
            ],
        ),
    ]