# Generated by Django 4.0.2 on 2022-03-25 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='名称')),
                ('describe', models.TextField(default='', null=True, verbose_name='描述')),
                ('is_delete', models.BooleanField(default=False, null=True, verbose_name='删除状态')),
                ('image', models.CharField(max_length=50, null=True, verbose_name='图片')),
                ('create_time', models.DateField(auto_now_add=True)),
                ('update_time', models.DateField(auto_now=True)),
            ],
        ),
    ]