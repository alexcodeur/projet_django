# saisie_budget/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.saisie_budget_home, name='saisie_budget_home'),
    path('delete/<int:entry_id>/', views.delete_entry, name='delete_entry'),
]
