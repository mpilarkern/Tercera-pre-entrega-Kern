# Generated by Django 4.2.6 on 2023-11-04 21:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control_blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Movies',
            new_name='Movie',
        ),
        migrations.RenameModel(
            old_name='Series',
            new_name='Serie',
        ),
    ]