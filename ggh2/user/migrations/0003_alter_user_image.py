# Generated by Django 3.2.6 on 2021-08-13 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_user_cabinet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, default='../static/img/default_img.jpg', upload_to='user'),
        ),
    ]
