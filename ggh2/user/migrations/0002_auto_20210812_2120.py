# Generated by Django 3.2.6 on 2021-08-12 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth',
            field=models.CharField(default='', max_length=9, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='cabinet',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='location',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(default='', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='ph_no',
            field=models.CharField(default='', max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_email',
            field=models.CharField(default='dydrkfsla0821@gmail.com', max_length=200, null=True),
        ),
    ]
