# Generated by Django 3.0.2 on 2020-01-21 22:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90)),
                ('date', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('course_full_img', models.ImageField(default='/images/test1.jpg', upload_to='images/')),
                ('overview', models.TextField()),
                ('course_type', models.CharField(choices=[('tech', 'Technical'), ('mangt', 'Managerial')], default='mangt', max_length=6)),
                ('date', models.DateField(null=True)),
                ('fees', models.DecimalField(decimal_places=2, max_digits=10000)),
                ('outline', models.TextField()),
                ('duration', models.IntegerField(default=5, verbose_name='Durations in Days')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Categorie')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('symbol', models.CharField(max_length=3)),
            ],
            options={
                'verbose_name_plural': 'Languages',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name_plural': 'Locations',
            },
        ),
        migrations.CreateModel(
            name='Course_Locality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('course_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.Course')),
                ('language', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.Language')),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.Location')),
            ],
            options={
                'verbose_name_plural': 'Course Localities',
            },
        ),
        migrations.AddField(
            model_name='course',
            name='location',
            field=models.ManyToManyField(to='courses.Course_Locality'),
        ),
    ]