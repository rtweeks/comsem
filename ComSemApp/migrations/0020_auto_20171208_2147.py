# Generated by Django 2.0 on 2017-12-08 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ComSemApp', '0019_auto_20171207_1825'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='description',
            field=models.CharField(default='pop', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tag',
            name='type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
