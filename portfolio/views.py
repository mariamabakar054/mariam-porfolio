from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy

from .forms import ContactForm
from .models import Message, Competence, Formation, Langue


# ─── Page d'accueil ───────────────────────────────────────────────────────────

def index(request):
    competences  = Competence.objects.all()
    formations   = Formation.objects.filter(type_entree='formation')
    experiences  = Formation.objects.filter(type_entree='experience')
    langues      = Langue.objects.all()

    # Données par défaut si la DB est vide (premier lancement)
    if not competences.exists():
        competences = [
            {'nom': 'HTML / CSS',   'niveau': 85, 'categorie': 'frontend'},
            {'nom': 'JavaScript',   'niveau': 65, 'categorie': 'frontend'},
            {'nom': 'Python',       'niveau': 60, 'categorie': 'backend'},
            {'nom': 'Django',       'niveau': 55, 'categorie': 'backend'},
            {'nom': 'PHP',          'niveau': 65, 'categorie': 'backend'},
            {'nom': 'MySQL',        'niveau': 65, 'categorie': 'database'},
        ]
    if not formations.exists():
        formations = [
            {'titre': 'Niveau 2 — Génie Logiciel',
             'etablissement': "Institut National de Science et Technique d'Abéché",
             'date_debut': '2023', 'date_fin': 'En cours', 'description': ''}
        ]
    if not experiences.exists():
        experiences = [
            {'titre': 'Stagiaire Développeuse Web',
             'etablissement': 'Expérience Tech, Abéché',
             'date_debut': '45 jours', 'date_fin': '',
             'description': 'Développement d\'un site vitrine en PHP/MySQL, conception d\'interfaces utilisateur modernes, gestion de l\'entreprise.'}
        ]
    if not langues.exists():
        langues = [
            {'nom': 'Français', 'niveau': 'Courant',       'pct': 90},
            {'nom': 'Arabe',    'niveau': 'Courant',        'pct': 90},
            {'nom': 'Anglais',  'niveau': 'Intermédiaire',  'pct': 55},
        ]

    return render(request, 'portfolio/index.html', {
        'competences': competences,
        'formations':  formations,
        'experiences': experiences,
        'langues':     langues,
    })


# ─── Contact ──────────────────────────────────────────────────────────────────

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre message a bien été envoyé ! Je vous répondrai bientôt.')
            return redirect('contact')
        else:
            messages.error(request, 'Veuillez corriger les erreurs dans le formulaire.')
    return render(request, 'portfolio/contact.html', {'form': form})


# ─── Connexion / Déconnexion ──────────────────────────────────────────────────

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    error = None
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        error = "Nom d'utilisateur ou mot de passe incorrect."
    return render(request, 'portfolio/login.html', {'error': error})


def logout_view(request):
    logout(request)
    return redirect('index')


# ─── Dashboard (protégé) ──────────────────────────────────────────────────────

@login_required
def dashboard(request):
    all_messages  = Message.objects.all()
    unread_count  = all_messages.filter(lu=False).count()
    competences   = Competence.objects.all()
    return render(request, 'portfolio/dashboard.html', {
        'messages_recus': all_messages,
        'unread_count':   unread_count,
        'competences':    competences,
    })


@login_required
def mark_read(request, pk):
    """Marque un message comme lu via POST."""
    if request.method == 'POST':
        Message.objects.filter(pk=pk).update(lu=True)
    return redirect('dashboard')
