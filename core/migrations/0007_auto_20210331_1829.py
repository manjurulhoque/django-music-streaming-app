# Generated by Django 3.1.7 on 2021-03-31 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20210331_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='thumbnail',
            field=models.ImageField(default='default.png', upload_to='artists'),
        ),
    ]
