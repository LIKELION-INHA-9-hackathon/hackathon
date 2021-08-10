# Generated by Django 3.2.6 on 2021-08-10 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wish_list',
            fields=[
                ('timestampmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='goods.timestampmodel')),
                ('goods_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.goods', verbose_name='찜한물품')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user', verbose_name='찜한사람')),
            ],
            bases=('goods.timestampmodel',),
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('timestampmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='goods.timestampmodel')),
                ('complete', models.IntegerField(choices=[(1, '공구완료'), (2, '공구진행'), (3, '완료임박')])),
                ('goods_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.goods', verbose_name='공구물품')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user', verbose_name='공구참여사람')),
            ],
            bases=('goods.timestampmodel',),
        ),
    ]