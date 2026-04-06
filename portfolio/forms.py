from django import forms
from .models import Message


class ContactForm(forms.ModelForm):
    class Meta:
        model  = Message
        fields = ['nom', 'email', 'sujet', 'message']
        widgets = {
            'nom':     forms.TextInput(attrs={'placeholder': 'Votre nom complet'}),
            'email':   forms.EmailInput(attrs={'placeholder': 'votre@email.com'}),
            'sujet':   forms.TextInput(attrs={'placeholder': 'Sujet de votre message'}),
            'message': forms.Textarea(attrs={
                'placeholder': 'Décrivez votre projet ou votre demande…',
                'rows': 6,
            }),
        }
        labels = {
            'nom':     'Nom complet',
            'email':   'Email',
            'sujet':   'Sujet',
            'message': 'Message',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.setdefault('class', 'form-input')
