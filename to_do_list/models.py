from django.db import models

CHOICES = [
    ('new', 'Новая'),
    ('in_process', 'В процессе'),
    ('done', 'Сделано'),
]

class Task(models.Model):
    description = models.CharField(max_length=200, null=False, blank=False, verbose_name="Описание")
    status =  models.CharField(max_length=30, choices=CHOICES, verbose_name="Статус", default="new")
    date_to_do = models.TextField(max_length=10, null=False, blank=False, verbose_name="Дата выполнения", help_text="YYYY-mm-dd")

    def __str__(self):
        return f"{self.description} - {self.date_to_do}"
