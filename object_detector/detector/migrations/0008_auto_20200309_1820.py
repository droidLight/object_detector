# Generated by Django 3.0.3 on 2020-03-09 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detector', '0007_imagemodel_input_threshold'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagemodel',
            name='input_threshold',
            field=models.FloatField(default=0.7),
        ),
    ]
