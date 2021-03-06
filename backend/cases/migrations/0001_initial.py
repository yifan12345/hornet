# Generated by Django 4.0.2 on 2022-03-30 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100, verbose_name='名称')),
                ('parent_id', models.IntegerField(default=0, verbose_name='父级ID')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除状态')),
                ('create_time', models.DateField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateField(auto_now=True, verbose_name='更新时间')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
            ],
        ),
    ]
