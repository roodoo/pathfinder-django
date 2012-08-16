# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Creature'
        db.create_table('creatures_creature', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('appearance', self.gf('django.db.models.fields.TextField')()),
            ('source', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('source_page', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('cr', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('subname', self.gf('django.db.models.fields.CharField')(max_length=40, blank=True)),
            ('xp', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('aura', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('alignment', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('size', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('creature_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='creatures', null=True, to=orm['creatures.CreatureType'])),
            ('initiative', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('senses', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('perception', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('ac', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('hp', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('fort', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('ref', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('will', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('resist', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('extra_defense', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('speed', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('melee', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('rrange', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('space', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('reach', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('extra_offense', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('strength', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('dexterity', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('constitution', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('intelligence', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('wisdom', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('charisma', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('bab', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('cmb', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('cmd', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('environment', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('organization', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('treasure', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal('creatures', ['Creature'])

        # Adding M2M table for field creature_subtypes on 'Creature'
        db.create_table('creatures_creature_creature_subtypes', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('creature', models.ForeignKey(orm['creatures.creature'], null=False)),
            ('creaturesubtype', models.ForeignKey(orm['creatures.creaturesubtype'], null=False))
        ))
        db.create_unique('creatures_creature_creature_subtypes', ['creature_id', 'creaturesubtype_id'])

        # Adding model 'CreatureType'
        db.create_table('creatures_creaturetype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('creatures', ['CreatureType'])

        # Adding model 'CreatureTypeFeature'
        db.create_table('creatures_creaturetypefeature', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creature_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['creatures.CreatureType'])),
            ('feature', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('creatures', ['CreatureTypeFeature'])

        # Adding model 'CreatureTypeTrait'
        db.create_table('creatures_creaturetypetrait', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creature_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['creatures.CreatureType'])),
            ('trait', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('creatures', ['CreatureTypeTrait'])

        # Adding model 'CreatureSubtype'
        db.create_table('creatures_creaturesubtype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('creatures', ['CreatureSubtype'])

        # Adding model 'CreatureSubtypeTrait'
        db.create_table('creatures_creaturesubtypetrait', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creature_subtype', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['creatures.CreatureSubtype'])),
            ('trait', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('creatures', ['CreatureSubtypeTrait'])


    def backwards(self, orm):
        
        # Deleting model 'Creature'
        db.delete_table('creatures_creature')

        # Removing M2M table for field creature_subtypes on 'Creature'
        db.delete_table('creatures_creature_creature_subtypes')

        # Deleting model 'CreatureType'
        db.delete_table('creatures_creaturetype')

        # Deleting model 'CreatureTypeFeature'
        db.delete_table('creatures_creaturetypefeature')

        # Deleting model 'CreatureTypeTrait'
        db.delete_table('creatures_creaturetypetrait')

        # Deleting model 'CreatureSubtype'
        db.delete_table('creatures_creaturesubtype')

        # Deleting model 'CreatureSubtypeTrait'
        db.delete_table('creatures_creaturesubtypetrait')


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
        }
    }

    complete_apps = ['creatures']
