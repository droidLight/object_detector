# Generated by Django 3.0.3 on 2020-03-09 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detector', '0005_delete_maskedimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagemodel',
            name='input_name',
            field=models.CharField(default='no_name', max_length=50),
            preserve_default=False,
        ),
    ]
