# Generated by Django 3.0.2 on 2020-02-02 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0015_auto_20200202_1617'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='courseinfo',
            options={'verbose_name_plural': 'Course Infomations'},
        ),
        migrations.RenameField(
            model_name='courseinfo',
            old_name='date',
            new_name='end_date',
        ),
        migrations.RemoveField(
            model_name='category',
            name='instructor_by_category',
        ),
        migrations.RemoveField(
            model_name='course',
            name='fees',
        ),
        migrations.RemoveField(
            model_name='course',
            name='instructor',
        ),
        migrations.RemoveField(
            model_name='mycourse',
            name='date',
        ),
        migrations.AddField(
            model_name='course',
            name='code',
            field=models.CharField(default='PRO101', max_length=10),
        ),
        migrations.AddField(
            model_name='course',
            name='label',
            field=models.CharField(default='Physical Event', max_length=20),
        ),
        migrations.AddField(
            model_name='courseinfo',
            name='start_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='mycourse',
            name='end_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='mycourse',
            name='start_date',
            field=models.DateField(null=True),
        ),
    ]
