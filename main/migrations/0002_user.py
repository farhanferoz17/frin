# Generated by Django 2.2.2 on 2019-07-03 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=200)),
                ('user_id', models.PositiveIntegerField()),
                ('user_desc', models.TextField()),
                ('user_email', models.CharField(max_length=200)),
                ('user_pass', models.CharField(max_length=200)),
                ('user_bd', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
