# Generated by Django 2.0 on 2018-08-25 20:35

from django.db import migrations


class Migration(migrations.Migration):

    def delete_attempt_duplicated(apps, schema_editor):
        StudentAttempt = apps.get_model("ComSemApp", "Worksheet")
        worksheets = Worksheet.objects.all()
        for worksheet in worksheets:
            topic = worksheet.topic
            if topic:
                worksheet.topic_char_field = topic.topic
                worksheet.save()

    dependencies = [
        ('ComSemApp', '0010_auto_20180825_0811'),
    ]

    operations = [
        migrations.RunPython(move_topic_table_to_charfield, reverse_func),
        migrations.AlterUniqueTogether(
            name='studentattempt',
            unique_together={('student_submission', 'expression')},
        ),
    ]