# Generated by Django 2.0.6 on 2019-01-23 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_kind',
            field=models.CharField(default='1', max_length=1),
        ),
    ]
