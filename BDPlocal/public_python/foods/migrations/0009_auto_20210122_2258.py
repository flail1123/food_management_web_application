# Generated by Django 2.2 on 2021-01-22 21:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0008_auto_20210122_2209'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foundationfood',
            name='food_id',
        ),
        migrations.DeleteModel(
            name='CustomFood',
        ),
        migrations.DeleteModel(
            name='FoundationFood',
        ),
    ]
