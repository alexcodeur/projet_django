# saisie_budget/models.py
from django.db import models

class BudgetEntry(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    date_soumission = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nom} - {self.date_soumission}'
