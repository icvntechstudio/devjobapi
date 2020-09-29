# Generated by Django 3.1.1 on 2020-09-29 14:54

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import jobs.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=150)),
                ('type', models.CharField(choices=[('Full Time', 'Full Time'), ('Part time', 'Part time'), ('Part time', 'Internship')], default='Full Time', max_length=10)),
                ('last_date', models.DateTimeField(blank=True, null=True)),
                ('company_name', models.CharField(max_length=100)),
                ('website', models.CharField(default='', max_length=100)),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, default=jobs.models.get_tag_default, size=None)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applicants', to='jobs.job')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.user')),
            ],
            options={
                'unique_together': {('user', 'job')},
            },
        ),
    ]
