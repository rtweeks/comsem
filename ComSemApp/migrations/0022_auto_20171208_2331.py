# Generated by Django 2.0 on 2017-12-08 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ComSemApp', '0021_auto_20171208_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='frequency',
            field=models.IntegerField(default=1),
        ),
    ]
