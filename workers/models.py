from django.db import models


class Worker(models.Model):
    """Модель работника."""

    id = models.IntegerField(
        primary_key=True, unique=True, verbose_name="ID", help_text="Введите ID"
    )
    full_name = models.CharField(
        max_length=100, verbose_name="ФИО", help_text="Введите ФИО"
    )
    brigade_number = models.IntegerField(
        verbose_name="Номер бригады", help_text="Введите номер бригады"
    )
    salary = models.DecimalField(
        max_digits=8, decimal_places=2, help_text="Введите зарплату"
    )
    specialization = models.CharField(
        max_length=50, verbose_name="Название работ", help_text="Введите название работ"
    )

    def __str__(self):
        return self.full_name
