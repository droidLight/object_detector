# Generated by Django 3.0.3 on 2020-03-10 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detector', '0008_auto_20200309_1820'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imagemodel',
            old_name='input_name',
            new_name='output_name',
        ),
    ]