from django import forms

from spells.models import Spell

class SpellForm(forms.ModelForm):

    class Meta:
        model = Spell

        widgets = {
            'effect': forms.Textarea(attrs={'rows': 3}),
            'spell_list': forms.CheckboxSelectMultiple(),
            'school': forms.RadioSelect(),
            'subschool': forms.CheckboxSelectMultiple(),
            'descriptor': forms.CheckboxSelectMultiple(),
            'description': forms.Textarea(attrs={'rows':10, 'cols':100}),
        }
#name
#effect

#spell_list

#source
#source_page

#school
#subschool
#descriptor

#casting_time
#components
#components_detail
#duration
#spell_range
#target
#area
#saving_throw
#spell_resistance

#description
