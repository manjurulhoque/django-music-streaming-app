# Generated by Django 3.1.7 on 2021-03-31 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20210331_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='thumbnail',
            field=models.ImageField(default='artists/default.png', upload_to='artists'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='thumbnail',
            field=models.ImageField(default='genres/default.png', upload_to='genres'),
        ),
    ]
