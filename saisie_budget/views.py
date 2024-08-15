# saisie_budget/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm
from .models import BudgetEntry

def saisie_budget_home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Sauvegarder les données dans la base de données
            BudgetEntry.objects.create(
                nom=form.cleaned_data['nom'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )
            return redirect('saisie_budget_home')  # Rediriger vers la même vue pour afficher les données
    else:
        form = ContactForm()

    # Récupérer les entrées de la base de données
    entries = BudgetEntry.objects.all()
    
    return render(request, 'saisie_budget/home.html', {'form': form, 'entries': entries})

def delete_entry(request, entry_id):
    entry = get_object_or_404(BudgetEntry, id=entry_id)
    entry.delete()
    return redirect('saisie_budget_home')
