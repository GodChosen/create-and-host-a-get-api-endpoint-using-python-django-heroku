# Generated by Django 4.1.2 on 2022-10-27 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SlackUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slackUsername', models.CharField(max_length=15)),
                ('backend', models.BooleanField()),
                ('age', models.IntegerField()),
                ('bio', models.CharField(max_length=600)),
            ],
        ),
    ]
