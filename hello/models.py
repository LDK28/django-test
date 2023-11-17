from django.db import models

class TestModel(models.Model):
    number = models.IntegerField(verbose_name='Число')
    string = models.TextField(verbose_name='Текст')
    file = models.FileField(verbose_name='Файлы', upload_to='files/', blank=True)

    def __str__(self):
        return 'Тест' + str(self.id)

    class Meta:
        verbose_name='Тестовая таблица'
        verbose_name_plural='Тестовые таблица'
