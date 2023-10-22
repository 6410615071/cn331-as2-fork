# Generated by Django 4.2.6 on 2023-10-22 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enrollment', '0002_class_enrolled_students'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='class_max_enroll',
            field=models.PositiveIntegerField(default=2),
        ),
        migrations.AlterField(
            model_name='class',
            name='class_status',
            field=models.CharField(choices=[('open', 'Open'), ('close', 'Close')], default='open', max_length=10),
        ),
        migrations.AlterField(
            model_name='class',
            name='class_year',
            field=models.PositiveIntegerField(default=2000),
        ),
    ]