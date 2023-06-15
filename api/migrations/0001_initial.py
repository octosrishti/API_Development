# Generated by Django 4.2.2 on 2023-06-15 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entyr_id', models.IntegerField(unique=True)),
                ('date', models.DateTimeField()),
                ('user', models.CharField(max_length=100)),
                ('software', models.CharField(max_length=50)),
                ('seats', models.IntegerField(blank=True, default=0, null=True)),
                ('amount', models.IntegerField(blank=True, default=0, null=True)),
            ],
            options={
                'verbose_name': 'maketing',
                'db_table': 'market_value',
            },
        ),
    ]
