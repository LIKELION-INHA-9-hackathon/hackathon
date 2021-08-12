# Generated by Django 3.2.6 on 2021-08-11 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_user_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('Male', '남자'), ('Female', '여자'), ('None', '선택안함')], default='', max_length=10),
        ),
    ]
