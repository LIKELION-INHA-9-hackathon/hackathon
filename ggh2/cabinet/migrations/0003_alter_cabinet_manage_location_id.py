# Generated by Django 3.2.6 on 2021-08-06 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabinet', '0002_auto_20210806_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cabinet_manage',
            name='location_id',
            field=models.IntegerField(),
        ),
    ]