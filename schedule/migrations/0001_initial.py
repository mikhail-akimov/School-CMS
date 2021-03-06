# Generated by Django 2.1.2 on 2018-10-05 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('delete_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('mainmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='schedule.MainModel')),
                ('name', models.CharField(max_length=4)),
            ],
            bases=('schedule.mainmodel',),
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('mainmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='schedule.MainModel')),
                ('les_grade', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='schedule.Grade')),
            ],
            bases=('schedule.mainmodel',),
        ),
        migrations.CreateModel(
            name='Pupil',
            fields=[
                ('mainmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='schedule.MainModel')),
                ('lastname', models.CharField(max_length=32)),
                ('firstname', models.CharField(max_length=32)),
                ('surname', models.CharField(max_length=32)),
                ('pup_grade', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='schedule.Grade')),
            ],
            bases=('schedule.mainmodel',),
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('mainmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='schedule.MainModel')),
                ('number', models.PositiveIntegerField(default=0)),
            ],
            bases=('schedule.mainmodel',),
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('mainmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='schedule.MainModel')),
                ('datetime', models.DateTimeField()),
                ('plan_lesson', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='schedule.Lesson')),
            ],
            bases=('schedule.mainmodel',),
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('mainmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='schedule.MainModel')),
                ('name', models.CharField(max_length=32)),
            ],
            bases=('schedule.mainmodel',),
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('mainmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='schedule.MainModel')),
                ('lastname', models.CharField(max_length=32)),
                ('firstname', models.CharField(max_length=32)),
                ('surname', models.CharField(max_length=32)),
            ],
            bases=('schedule.mainmodel',),
        ),
        migrations.AddField(
            model_name='subject',
            name='subj_teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='schedule.Teacher'),
        ),
        migrations.AddField(
            model_name='room',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='schedule.Teacher'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='les_room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='schedule.Room'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='les_subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='schedule.Subject'),
        ),
        migrations.AddField(
            model_name='grade',
            name='lead',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='schedule.Teacher'),
        ),
    ]
