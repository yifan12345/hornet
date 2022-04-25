# Generated by Django 4.0.2 on 2022-04-15 01:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='名称')),
                ('url', models.TextField(verbose_name='URL')),
                ('method', models.CharField(max_length=10, verbose_name='请求方法')),
                ('header', models.CharField(default='{}', max_length=1000, null=True, verbose_name='请求体')),
                ('params_type', models.CharField(max_length=10, verbose_name='参数类型')),
                ('params_body', models.TextField(default='{}', null=True, verbose_name='参数内容')),
                ('result', models.TextField(default='{}', null=True, verbose_name='结果')),
                ('assert_type', models.CharField(max_length=10, null=True, verbose_name='断言类型')),
                ('assert_text', models.TextField(default='{}', null=True, verbose_name='断言结果')),
                ('is_Delete', models.BooleanField(default=False, verbose_name='状态')),
                ('create_time', models.DateField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateField(auto_now=True, verbose_name='更新时间')),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cases.module')),
            ],
        ),
    ]
