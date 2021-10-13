from typing import Text
from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User


class Topic(models.Model):
    """"Um assunto sobre o qual o usuário está aprendendo."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=CASCADE)

    def __str__(self) -> str:
        """Devolve uma representação em string do modelo."""
        return self.text


class Entry(models.Model):
    """Algo específico aprendido sobre o assunto."""
    topic = models.ForeignKey(Topic, on_delete=CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self) -> str:
        """Devolve um representação em string do modelo"""
        return self.text[:50] + '...'
