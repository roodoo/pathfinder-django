from django.db import models

ABILITY_CHOICES = (
    ('Str', 'Strength'),
    ('Dex', 'Dexterity'),
    ('Con', 'Constitution'),
    ('Int', 'Intelligence'),
    ('Wis', 'Wisdom'),
    ('Cha', 'Charisma')
)

class Skill(models.Model):

    name = models.CharField(max_length=30)
    option = models.BooleanField(default=False)
    description = models.TextField()
    category = models.CharField(max_length=30, blank=True)
    untrained = models.BooleanField(default=False)
    armor_check_penalty = models.BooleanField(default=False)
    ability = models.CharField(max_length=10, choices=ABILITY_CHOICES)

    source = models.CharField(max_length=30)
    source_page = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

