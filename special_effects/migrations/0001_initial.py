# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SpecialEffects'
        db.create_table(u'special_effects_specialeffects', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('imgfile', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('thumbnail', self.gf('django.db.models.fields.files.ImageField')(max_length=500, null=True, blank=True)),
            ('position', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal(u'special_effects', ['SpecialEffects'])


    def backwards(self, orm):
        # Deleting model 'SpecialEffects'
        db.delete_table(u'special_effects_specialeffects')


    models = {
        u'special_effects.specialeffects': {
            'Meta': {'ordering': "['position']", 'object_name': 'SpecialEffects'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imgfile': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['special_effects']