from django import forms
from .models import Team

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name']
        labels = {
            'name': 'Название команды',  # Здесь меняем текст метки на "Название команды"
        }

class PreferencesForm(forms.Form):
    THEME_CHOICES = [
        ('light', 'Светлая'),
        ('dark', 'Темная'),
    ]
    LANGUAGE_CHOICES = [
        ('en', 'Английский'),
        ('ru', 'Русский'),
    ]

    theme = forms.ChoiceField(choices=THEME_CHOICES, label='Выберите тему:')
    language = forms.ChoiceField(choices=LANGUAGE_CHOICES, label='Выберите язык:')