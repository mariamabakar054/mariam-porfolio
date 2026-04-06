from django.db import models
from django.utils import timezone


class Message(models.Model):
    """Messages reçus via le formulaire de contact."""
    nom     = models.CharField(max_length=100, verbose_name="Nom")
    email   = models.EmailField(verbose_name="Email")
    sujet   = models.CharField(max_length=200, verbose_name="Sujet")
    message = models.TextField(verbose_name="Message")
    lu      = models.BooleanField(default=False, verbose_name="Lu")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Reçu le")

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.nom} — {self.sujet}"


class Competence(models.Model):
    """Compétences techniques affichées sur le portfolio."""
    CATEGORIES = [
        ('frontend', 'Frontend'),
        ('backend',  'Backend'),
        ('database', 'Base de données'),
        ('other',    'Autre'),
    ]
    nom       = models.CharField(max_length=100)
    niveau    = models.PositiveSmallIntegerField(help_text="Niveau de 0 à 100")
    categorie = models.CharField(max_length=20, choices=CATEGORIES, default='other')
    ordre     = models.PositiveSmallIntegerField(default=0)

    class Meta:
        verbose_name = "Compétence"
        ordering = ['ordre', 'nom']

    def __str__(self):
        return self.nom


class Formation(models.Model):
    """Entrées de formation / expérience."""
    TYPES = [('formation', 'Formation'), ('experience', 'Expérience')]
    type_entree  = models.CharField(max_length=20, choices=TYPES, default='formation')
    titre        = models.CharField(max_length=200)
    etablissement= models.CharField(max_length=300)
    date_debut   = models.CharField(max_length=30)   # ex: "2026"
    date_fin     = models.CharField(max_length=30, blank=True, default='En cours')
    description  = models.TextField(blank=True)
    ordre        = models.PositiveSmallIntegerField(default=0)

    class Meta:
        verbose_name = "Formation / Expérience"
        ordering = ['ordre']

    def __str__(self):
        return self.titre


class Langue(models.Model):
    nom     = models.CharField(max_length=50)
    niveau  = models.CharField(max_length=50)   # ex: "Courant"
    pct     = models.PositiveSmallIntegerField(default=70, help_text="% pour la barre")
    ordre   = models.PositiveSmallIntegerField(default=0)

    class Meta:
        verbose_name = "Langue"
        ordering = ['ordre']

    def __str__(self):
        return self.nom
