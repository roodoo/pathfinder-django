from django.db import models

ALIGNMENT_CHOICES = (
    ('CE', 'CE'),
    ('CN', 'CN'),
    ('CG', 'CG'),
    ('NE', 'NE'),
    ('N', 'N'),
    ('NG', 'NG'),
    ('LE', 'LE'),
    ('LN', 'LN'),
    ('LG', 'LG')
)
SIZE_CHOICES = (
    ('F', 'Fine'),
    ('D', 'Diminutive'),
    ('T', 'Tiny'),
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
    ('H', 'Huge'),
    ('G', 'Gargantuan'),
    ('C', 'Colossal')
)


class Creature(models.Model):

    name = models.CharField(max_length=100)
    appearance = models.TextField()

    #TODOdescription = models.TextField()

    source = models.CharField(max_length=30, blank=True)
    source_page = models.CharField(max_length=10, blank=True)

    cr = models.CharField(max_length=10)
    subname = models.CharField(max_length=40, blank=True)
    xp = models.PositiveIntegerField()
    aura = models.CharField(max_length=20, blank=True)

    alignment = models.CharField(max_length=2, choices=ALIGNMENT_CHOICES)
    size = models.CharField(max_length=1, choices=SIZE_CHOICES)

    category = models.CharField(max_length=30, blank=True)

    creature_type = models.ForeignKey('creatures.CreatureType', null=True, related_name="creatures")
    creature_subtypes = models.ManyToManyField('creatures.CreatureSubtype', related_name="creatures")

    initiative = models.CharField(max_length=30)
    senses = models.CharField(max_length=100, blank=True)
    perception = models.CharField(max_length=30)

    ## defense
    ac = models.CharField(max_length=100)
    hp = models.CharField(max_length=100)

    fort = models.CharField(max_length=30)
    ref = models.CharField(max_length=30)
    will = models.CharField(max_length=30)

    # probably more here TODO
    resist = models.CharField(max_length=100, blank=True)

    extra_defense = models.TextField(blank=True)

    ## offense
    speed = models.CharField(max_length=100, blank=True)
    melee = models.CharField(max_length=100, blank=True)
    rrange = models.CharField(max_length=100, blank=True)
    #TODOranged = models.CharField(max_length=100, blank=True)
    space = models.CharField(max_length=20, blank=True)
    reach = models.CharField(max_length=20, blank=True)

    extra_offense = models.TextField(blank=True)

    ## statistics
    strength = models.CharField(max_length=30)
    dexterity = models.CharField(max_length=30)
    constitution = models.CharField(max_length=30)
    intelligence = models.CharField(max_length=30)
    wisdom = models.CharField(max_length=30)
    charisma = models.CharField(max_length=30)

    bab = models.CharField(max_length=20)
    cmb = models.CharField(max_length=40)
    cmd = models.CharField(max_length=40)

    # feats
    # languages

    ## ecology
    # TODO something different here
    environment = models.CharField(max_length=100, blank=True)
    organization = models.CharField(max_length=100, blank=True)
    treasure = models.CharField(max_length=100, blank=True)

    ## special abilities
    # TODO these will be different too

    def __unicode__(self):
        return self.name

    class Meta:
        get_latest_by = 'id'


class CreatureType(models.Model):

    name = models.CharField(max_length=30)
    description = models.TextField()

    def __unicode__(self):
        return self.name

class CreatureTypeFeature(models.Model):

    creature_type = models.ForeignKey('creatures.CreatureType')
    feature = models.TextField()

class CreatureTypeTrait(models.Model):

    creature_type = models.ForeignKey('creatures.CreatureType')
    trait = models.TextField()

class CreatureSubtype(models.Model):

    name = models.CharField(max_length=30)
    description = models.TextField()

    def __unicode__(self):
        return self.name

class CreatureSubtypeTrait(models.Model):

    creature_subtype = models.ForeignKey('creatures.CreatureSubtype')
    trait = models.TextField()

#########

class CreatureSkill(models.Model):
    creature = models.ForeignKey('creatures.Creature', related_name="skills")
    skill = models.ForeignKey('skills.Skill')
    option = models.CharField(max_length=30, blank=True)
    modifier = models.CharField(max_length=10)

    #TODOdetails = models.CharField(max_length=100)

    def __unicode__(self):
        out = str(self.skill)
        if self.skill.option:
            out += " (%s)" % self.option
        out += " %s" % self.modifier
        return out

#########



