# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'CreatureSkill'
        db.create_table('creatures_creatureskill', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creature', self.gf('django.db.models.fields.related.ForeignKey')(related_name='skills', to=orm['creatures.Creature'])),
            ('skill', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['skills.Skill'])),
            ('option', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('modifier', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('creatures', ['CreatureSkill'])


    def backwards(self, orm):
        
        # Deleting model 'CreatureSkill'
        db.delete_table('creatures_creatureskill')


    models = {
        'creatures.creature': {
            'Meta': {'object_name': 'Creature'},
            'ac': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'alignment': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'appearance': ('django.db.models.fields.TextField', [], {}),
            'aura': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'bab': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'category': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'charisma': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'cmb': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'cmd': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'constitution': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'cr': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'creature_subtypes': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'creatures'", 'symmetrical': 'False', 'to': "orm['creatures.CreatureSubtype']"}),
            'creature_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'creatures'", 'null': 'True', 'to': "orm['creatures.CreatureType']"}),
            'dexterity': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'environment': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'extra_defense': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'extra_offense': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'fort': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'hp': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'initiative': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'intelligence': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'melee': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'organization': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'perception': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'reach': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'ref': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'resist': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'rrange': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'senses': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'source_page': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'space': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'speed': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'strength': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'subname': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'treasure': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'will': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'wisdom': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'xp': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        'creatures.creatureskill': {
            'Meta': {'object_name': 'CreatureSkill'},
            'creature': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'skills'", 'to': "orm['creatures.Creature']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modifier': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'option': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'skill': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['skills.Skill']"})
        },
        'creatures.creaturesubtype': {
            'Meta': {'object_name': 'CreatureSubtype'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'creatures.creaturesubtypetrait': {
            'Meta': {'object_name': 'CreatureSubtypeTrait'},
            'creature_subtype': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['creatures.CreatureSubtype']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'trait': ('django.db.models.fields.TextField', [], {})
        },
        'creatures.creaturetype': {
            'Meta': {'object_name': 'CreatureType'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'creatures.creaturetypefeature': {
            'Meta': {'object_name': 'CreatureTypeFeature'},
            'creature_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['creatures.CreatureType']"}),
            'feature': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'creatures.creaturetypetrait': {
            'Meta': {'object_name': 'CreatureTypeTrait'},
            'creature_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['creatures.CreatureType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'trait': ('django.db.models.fields.TextField', [], {})
        },
        'skills.skill': {
            'Meta': {'object_name': 'Skill'},
            'ability': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'armor_check_penalty': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'category': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'option': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'source_page': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'untrained': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['creatures']
