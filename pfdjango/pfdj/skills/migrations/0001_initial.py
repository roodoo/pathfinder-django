# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Skill'
        db.create_table('skills_skill', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('option', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('untrained', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('armor_check_penalty', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('ability', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('source', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('source_page', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('skills', ['Skill'])


    def backwards(self, orm):
        
        # Deleting model 'Skill'
        db.delete_table('skills_skill')


    models = {
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

    complete_apps = ['skills']
