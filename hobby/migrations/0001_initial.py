# Generated by Django 3.2.16 on 2022-10-07 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HobbiesTmp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hobby', models.CharField(blank=True, max_length=30, null=True)),
                ('outdoor', models.IntegerField(blank=True, null=True)),
                ('team', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'hobbies_tmp',
                'managed': False,
            },
        ),
    ]
