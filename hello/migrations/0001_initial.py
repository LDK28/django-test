# Generated by Django 4.2.4 on 2023-11-17 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='Число')),
                ('string', models.TextField(verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Тестовая таблица',
            },
        ),
    ]
