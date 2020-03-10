# Generated by Django 3.0.3 on 2020-03-09 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detector', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaskedImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MaskedImage', models.ImageField(upload_to='masked_images')),
            ],
        ),
        migrations.AlterField(
            model_name='imagemodel',
            name='input_image',
            field=models.ImageField(upload_to='uploaded_images'),
        ),
    ]