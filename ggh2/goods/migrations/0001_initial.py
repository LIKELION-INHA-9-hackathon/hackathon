# Generated by Django 3.2.6 on 2021-08-13 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cabinet', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TimeStampModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('timestampmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='goods.timestampmodel')),
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('type', models.CharField(choices=[('냉장', '냉장상품'), ('냉동', '냉동식품'), ('그외', '그 외 모두')], max_length=10)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('recruitment_no', models.IntegerField()),
                ('expired', models.CharField(max_length=9)),
                ('pre_people', models.IntegerField()),
                ('ori_price', models.IntegerField()),
                ('description', models.TextField()),
                ('due_date', models.CharField(max_length=8)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='thumbnail')),
                ('cabinet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cabinet.cabinet_manage', verbose_name='배송지')),
                ('category', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to='goods.category')),
                ('uploader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user', verbose_name='작성자')),
            ],
            bases=('goods.timestampmodel',),
        ),
        migrations.CreateModel(
            name='Goods_img',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otherimg', models.ImageField(blank=True, null=True, upload_to='goods')),
                ('goods_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.goods')),
            ],
        ),
        migrations.CreateModel(
            name='Goods_comments',
            fields=[
                ('timestampmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='goods.timestampmodel')),
                ('content', models.TextField()),
                ('goods_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods_comment', to='goods.goods', verbose_name='댓글')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user', verbose_name='작성자')),
            ],
            bases=('goods.timestampmodel',),
        ),
    ]
