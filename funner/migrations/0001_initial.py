# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('client', models.ForeignKey(to='funner.Client')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TestBase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('end_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('testbase_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='funner.TestBase')),
                ('domain', models.ForeignKey(to='funner.Domain')),
            ],
            options={
            },
            bases=('funner.testbase',),
        ),
        migrations.CreateModel(
            name='TestResult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('expectation', models.CharField(max_length=200)),
                ('actual', models.CharField(max_length=200)),
                ('success', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TestRun',
            fields=[
                ('testbase_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='funner.TestBase')),
                ('scenarios_only', models.BooleanField(default=False)),
                ('content_checks_only', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=('funner.testbase',),
        ),
        migrations.CreateModel(
            name='Validation',
            fields=[
                ('testresult_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='funner.TestResult')),
                ('testcase', models.ForeignKey(to='funner.TestCase')),
            ],
            options={
            },
            bases=('funner.testresult',),
        ),
        migrations.AddField(
            model_name='testcase',
            name='testresult',
            field=models.ForeignKey(to='funner.TestResult'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testcase',
            name='testrun',
            field=models.ForeignKey(to='funner.TestRun'),
            preserve_default=True,
        ),
    ]
