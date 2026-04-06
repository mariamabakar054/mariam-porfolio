from django.contrib import admin
from .models import Message, Competence, Formation, Langue


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display  = ('nom', 'email', 'sujet', 'lu', 'created_at')
    list_filter   = ('lu',)
    search_fields = ('nom', 'email', 'sujet')
    readonly_fields = ('created_at',)
    actions = ['marquer_lu']

    @admin.action(description='Marquer comme lu')
    def marquer_lu(self, request, queryset):
        queryset.update(lu=True)


@admin.register(Competence)
class CompetenceAdmin(admin.ModelAdmin):
    list_display  = ('nom', 'categorie', 'niveau', 'ordre')
    list_editable = ('niveau', 'ordre')


@admin.register(Formation)
class FormationAdmin(admin.ModelAdmin):
    list_display  = ('titre', 'type_entree', 'etablissement', 'date_debut', 'date_fin')
    list_filter   = ('type_entree',)


@admin.register(Langue)
class LangueAdmin(admin.ModelAdmin):
    list_display  = ('nom', 'niveau', 'pct', 'ordre')
    list_editable = ('pct', 'ordre')
