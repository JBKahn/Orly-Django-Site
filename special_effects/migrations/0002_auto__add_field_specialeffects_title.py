# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'SpecialEffects.title'
        db.add_column(u'special_effects_specialeffects', 'title',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'SpecialEffects.title'
        db.delete_column(u'special_effects_specialeffects', 'title')


    models = {
        u'special_effects.specialeffects': {
            'Meta': {'ordering': "['position']", 'object_name': 'SpecialEffects'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imgfile': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'})
        }
    }

    complete_apps = ['special_effects']