from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic.simple import direct_to_template

from creatures.forms import CreatureForm
from creatures.models import Creature

def index(request, template_name="creatures/default.html"):

    creatures = Creature.objects.all()

    context = {
        "creatures": creatures
    }
    return direct_to_template(request, template_name, extra_context=context)


def creature_details(request, creature_id, 
        template_name="creatures/creature_details.html"):

    creature = get_object_or_404(Creature, id=creature_id)

    context = {
        "creature": creature
    }
    return direct_to_template(request, template_name, extra_context=context)

def creature_edit(request, creature_id, 
        template_name="creatures/creature_edit.html"):

    creature = get_object_or_404(Creature, id=creature_id)
    
    if request.method == "POST":
        if "cancel" in request.POST:
            return HttpResponseRedirect(reverse("creatures"))

        form = CreatureForm(request.POST, instance=creature)
        if form.is_valid():
            creature = form.save()
            return HttpResponseRedirect(reverse("creatures-details", args=(creature.id,)))
    else:
        form = CreatureForm(instance=creature)

    context = {
        "creature": creature,
        "form": form
    }
    return direct_to_template(request, template_name, extra_context=context)

def creature_create(request, template_name="creatures/creature_edit.html"):

    if request.method == "POST":
        if "cancel" in request.POST:
            return HttpResponseRedirect(reverse("creatures"))

        form = CreatureForm(request.POST)
        if form.is_valid():
            creature = form.save()
            return HttpResponseRedirect(reverse("creatures-details", args=(creature.id,)))
    else:
        form = CreatureForm()

    context = {
        "form": form
    }
    return direct_to_template(request, template_name, extra_context=context)

