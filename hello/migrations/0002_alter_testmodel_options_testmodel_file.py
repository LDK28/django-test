# Generated by Django 4.2.4 on 2023-11-17 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='testmodel',
            options={'verbose_name': 'Тестовая таблица', 'verbose_name_plural': 'Тестовые таблица'},
        ),
        migrations.AddField(
            model_name='testmodel',
            name='file',
            field=models.FileField(blank=True, upload_to='files/', verbose_name='Файлы'),
        ),
    ]
