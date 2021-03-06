# Generated by Django 2.0.6 on 2019-01-23 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_code', models.CharField(blank=True, max_length=15, null=True)),
                ('p_name', models.CharField(blank=True, max_length=30, null=True)),
                ('start_date', models.CharField(blank=True, max_length=20, null=True)),
                ('earning', models.CharField(blank=True, max_length=20, null=True)),
                ('earn_7d', models.CharField(blank=True, max_length=20, null=True)),
                ('earn_14d', models.CharField(blank=True, max_length=20, null=True)),
                ('earn_28d', models.CharField(blank=True, max_length=20, null=True)),
                ('earn_35d', models.CharField(blank=True, max_length=20, null=True)),
                ('path_1m', models.CharField(blank=True, max_length=20, null=True)),
                ('path_3m', models.CharField(blank=True, max_length=20, null=True)),
                ('path_6m', models.CharField(blank=True, max_length=20, null=True)),
                ('path_1y', models.CharField(blank=True, max_length=20, null=True)),
                ('start_money', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'products',
            },
        ),
    ]
