# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Spell'
        db.create_table('spells_spell', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('effect', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('source', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('source_page', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('school', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['spells.School'], null=True)),
            ('casting_time', self.gf('django.db.models.fields.CharField')(max_length=100, null=True)),
            ('components', self.gf('django.db.models.fields.CharField')(max_length=40, null=True)),
            ('components_detail', self.gf('django.db.models.fields.CharField')(max_length=100, null=True)),
            ('duration', self.gf('django.db.models.fields.CharField')(max_length=100, null=True)),
            ('spell_range', self.gf('django.db.models.fields.CharField')(max_length=100, null=True)),
            ('target', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
            ('area', self.gf('django.db.models.fields.CharField')(max_length=100, null=True)),
            ('saving_throw', self.gf('django.db.models.fields.CharField')(max_length=100, null=True)),
            ('spell_resistance', self.gf('django.db.models.fields.CharField')(max_length=100, null=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('spells', ['Spell'])

        # Adding M2M table for field spell_list on 'Spell'
        db.create_table('spells_spell_spell_list', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('spell', models.ForeignKey(orm['spells.spell'], null=False)),
            ('spelllist', models.ForeignKey(orm['spells.spelllist'], null=False))
        ))
        db.create_unique('spells_spell_spell_list', ['spell_id', 'spelllist_id'])

        # Adding M2M table for field subschool on 'Spell'
        db.create_table('spells_spell_subschool', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('spell', models.ForeignKey(orm['spells.spell'], null=False)),
            ('subschool', models.ForeignKey(orm['spells.subschool'], null=False))
        ))
        db.create_unique('spells_spell_subschool', ['spell_id', 'subschool_id'])

        # Adding M2M table for field descriptor on 'Spell'
        db.create_table('spells_spell_descriptor', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('spell', models.ForeignKey(orm['spells.spell'], null=False)),
            ('descriptor', models.ForeignKey(orm['spells.descriptor'], null=False))
        ))
        db.create_unique('spells_spell_descriptor', ['spell_id', 'descriptor_id'])

        # Adding model 'School'
        db.create_table('spells_school', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('spells', ['School'])

        # Adding model 'SubSchool'
        db.create_table('spells_subschool', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('school', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['spells.School'])),
        ))
        db.send_create_signal('spells', ['SubSchool'])

        # Adding model 'Descriptor'
        db.create_table('spells_descriptor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('spells', ['Descriptor'])

        # Adding model 'SpellList'
        db.create_table('spells_spelllist', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('class_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('level', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal('spells', ['SpellList'])


    def backwards(self, orm):
        
        # Deleting model 'Spell'
        db.delete_table('spells_spell')

        # Removing M2M table for field spell_list on 'Spell'
        db.delete_table('spells_spell_spell_list')

        # Removing M2M table for field subschool on 'Spell'
        db.delete_table('spells_spell_subschool')

        # Removing M2M table for field descriptor on 'Spell'
        db.delete_table('spells_spell_descriptor')

        # Deleting model 'School'
        db.delete_table('spells_school')

        # Deleting model 'SubSchool'
        db.delete_table('spells_subschool')

        # Deleting model 'Descriptor'
        db.delete_table('spells_descriptor')

        # Deleting model 'SpellList'
        db.delete_table('spells_spelllist')


    models = {
        'spells.descriptor': {
            'Meta': {'object_name': 'Descriptor'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'spells.school': {
            'Meta': {'object_name': 'School'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'spells.spell': {
            'Meta': {'object_name': 'Spell'},
            'area': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'casting_time': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'components': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True'}),
            'components_detail': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'descriptor': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['spells.Descriptor']", 'symmetrical': 'False'}),
            'duration': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'effect': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'saving_throw': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['spells.School']", 'null': 'True'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'source_page': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'spell_list': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'spells'", 'symmetrical': 'False', 'to': "orm['spells.SpellList']"}),
            'spell_range': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'spell_resistance': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'subschool': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['spells.SubSchool']", 'symmetrical': 'False'}),
            'target': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'})
        },
        'spells.spelllist': {
            'Meta': {'object_name': 'SpellList'},
            'class_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        'spells.subschool': {
            'Meta': {'object_name': 'SubSchool'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['spells.School']"})
        }
    }

    complete_apps = ['spells']
