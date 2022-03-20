from django.db import models
from django.contrib.auth.models import User


class TestResults(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='test_author', verbose_name='Автор')
    portfolio_type = models.CharField(max_length=250, verbose_name='Тип портфеля')
    investment_horizon = models.CharField(max_length=250, verbose_name='Горизонт инвестирования')
    investment_amount = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Результаты теста"
        verbose_name = "Результат теста"
        ordering = ('-created',)

    def __str__(self):
        return f"{self.author} {self.created}"