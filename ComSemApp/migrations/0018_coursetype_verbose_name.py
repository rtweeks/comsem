# Generated by Django 2.0 on 2017-12-07 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ComSemApp', '0017_auto_20171207_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursetype',
            name='verbose_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
