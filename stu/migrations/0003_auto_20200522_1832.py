# Generated by Django 3.0.5 on 2020-05-22 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stu', '0002_auto_20200522_1826'),
    ]

    operations = [
        migrations.CreateModel(
            name='classes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='teachers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='teacher_class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stu.classes')),
                ('teacherID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stu.teachers')),
            ],
            options={
                'unique_together': {('classID', 'teacherID')},
            },
        ),
        migrations.CreateModel(
            name='students',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('classID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stu.classes')),
            ],
        ),
        migrations.AddField(
            model_name='classes',
            name='m',
            field=models.ManyToManyField(through='stu.teacher_class', to='stu.teachers'),
        ),
    ]
