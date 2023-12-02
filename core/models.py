from django.db import models

class Menu(models.Model):
    title = models.CharField(max_length=128, verbose_name='Название товара')
    image = models.ImageField(null=True, blank=True, upload_to="menu/")
    content = models.TextField('Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'Товар'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товар'

    def __str__(self):
        return f'Название товара {self.title}'
