# Generated by Django 3.1.8 on 2021-07-28 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flashcard_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='answer',
            new_name='back_content',
        ),
        migrations.RenameField(
            model_name='card',
            old_name='question',
            new_name='front_content',
        ),
    ]