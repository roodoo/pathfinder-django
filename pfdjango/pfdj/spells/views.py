from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic.simple import direct_to_template

from spells.forms import SpellForm
from spells.models import Spell, SpellList


def spells(request, template_name="spells/default.html"):
    """
    """
    spells = Spell.objects.all()

    context = {
        "spells": spells
    }
    return direct_to_template(request, template_name, extra_context=context)

#######3

def spell_details(request, spell_id, template_name="spells/details.html"):
    """
    """
    spell = get_object_or_404(Spell, id=spell_id)

    context = {
        "spell": spell
    }
    return direct_to_template(request, template_name, extra_context=context)

def spell_edit(request, spell_id, template_name="spells/edit.html"):
    """
    """
    spell = get_object_or_404(Spell, id=spell_id)
    
    if request.method == "POST":
        if "cancel" in request.POST:
            return HttpResponseRedirect(reverse("spells"))

        form = SpellForm(request.POST, instance=spell)
        if form.is_valid():
            spell = form.save()
            return HttpResponseRedirect(reverse("spell-details", args=(spell.id,)))
    else:
        form = SpellForm(instance=spell)
    context = {
        "spell": spell,
        "form": form
    }
    return direct_to_template(request, template_name, extra_context=context)

###############333

def spell_list(request, class_slug, level=None, 
        template_name="spells/list.html"):
    """
    """
    spell_lists = SpellList.objects.get_by_slug(class_slug)

    if level is not None:
        spell_lists = spell_list.filter(level=level)

    context = {
        "spell_lists": spell_lists
    }
    return direct_to_template(request, template_name, extra_context=context)
