# Generated by Django 3.2.6 on 2021-08-12 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20210812_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth',
            field=models.CharField(default='', max_length=9),
        ),
        migrations.AlterField(
            model_name='user',
            name='cabinet',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='location',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='ph_no',
            field=models.CharField(default='', max_length=11),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_email',
            field=models.CharField(default='dydrkfsla0821@gmail.com', max_length=200),
        ),
    ]
