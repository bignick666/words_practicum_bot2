from django.db import models


class Word(models.Model):
    CATS = [
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),
        ('Insane', 'Insane'),
    ]

    name = models.CharField(max_length=50, verbose_name='Слово')
    translate = models.CharField(max_length=50, verbose_name='Перевод')
    category = models.CharField(max_length=40, choices=CATS, verbose_name='Категория')

    class Meta:
        verbose_name = 'Слово'
        verbose_name_plural = 'Слова'
        db_table = 'words'
