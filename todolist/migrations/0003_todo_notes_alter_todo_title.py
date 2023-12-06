# Generated by Django 4.2.7 on 2023-12-04 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_rename_text_todo_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
