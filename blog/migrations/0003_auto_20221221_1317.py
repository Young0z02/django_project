# Generated by Django 3.1.5 on 2022-12-21 04:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_board_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='board',
        ),
        migrations.DeleteModel(
            name='Board',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
