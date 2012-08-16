from django.db import models

class Spell(models.Model):

    name = models.CharField(max_length=100)
    effect = models.CharField(max_length=300)

    spell_list = models.ManyToManyField('spells.SpellList', related_name="spells")

    source = models.CharField(max_length=30) # selection
    source_page = models.CharField(max_length=10)

    school = models.ForeignKey('spells.School', null=True)
    subschool = models.ManyToManyField('spells.SubSchool')
    descriptor = models.ManyToManyField('spells.Descriptor')

    casting_time = models.CharField(max_length=100, null=True)
    components = models.CharField(max_length=40, null=True)
    components_detail = models.CharField(max_length=100, null=True)
    duration = models.CharField(max_length=100, null=True)
    spell_range = models.CharField(max_length=100, null=True)
    target = models.CharField(max_length=200, null=True)
    area = models.CharField(max_length=100, null=True)
    saving_throw = models.CharField(max_length=100, null=True)
    spell_resistance = models.CharField(max_length=100, null=True)

    description = models.TextField()

    def display_school(self):
        out = None
        if self.school:
            out = self.school
            if self.subschool.count() > 0:
                out += " (%s)" % (",".join(self.subschool.all()))
            for descriptor in self.descriptor.all():
                out += " [%s]" % descriptor
        return out

    def __unicode__(self):
        return self.name

    class Meta:
        get_latest_by = 'id'
        ordering = ('name',)

class School(models.Model):

    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name

class SubSchool(models.Model):

    name = models.CharField(max_length=20)
    school = models.ForeignKey('spells.School')

    def __unicode__(self):
        return self.name

class Descriptor(models.Model):

    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name

###############3

class SpellListManager(models.Manager):

    def get_by_slug(self, slug):
        try:
            return {
                "alchemist": self.filter(class_name="Alchemist"),
                "antipaladin": self.filter(class_name="Antipaladin"),
                "bard": self.filter(class_name="Bard"),
                "cleric": self.filter(class_name="Cleric"),
                "druid": self.filter(class_name="Druid"),
                "elementalist_wizard": self.filter(class_name="Elementalist Wizard"),
                "inquisitor": self.filter(class_name="Inquisitor"),
                "magus": self.filter(class_name="Magus"),
                "paladin": self.filter(class_name="Paladin"),
                "ranger": self.filter(class_name="Ranger"),
                "sorcerer": self.filter(class_name="Sorcerer"),
                "summoner": self.filter(class_name="Summoner"),
                "witch": self.filter(class_name="Witch"),
                "wizard": self.filter(class_name="Wizard"),
                "oracle": self.filter(class_name="Oracle")
            }[slug]
        except KeyError:
            return self.none()

class SpellList(models.Model):

    class_name = models.CharField(max_length=20)
    level = models.PositiveIntegerField()

    objects = SpellListManager()

    def slug(self):
        return self.class_name.lower().replace(" ", "_")

    def __unicode__(self):
        return "%s %s" % (self.class_name, str(self.level))

    class Meta:
        get_latest_by = 'id'
        ordering = ('class_name', 'level')

