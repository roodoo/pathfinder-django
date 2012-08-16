from django import forms

from creatures.models import Creature

class CreatureForm(forms.ModelForm):

    class Meta:
        model = Creature
