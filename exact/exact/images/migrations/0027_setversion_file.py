# Generated by Django 3.0 on 2020-05-02 11:20

from django.db import migrations, models
import exact.images.models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0026_setversion_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='setversion',
            name='file',
            field=models.FileField(null=True, upload_to=exact.images.models.version_directory_path),
        ),
    ]