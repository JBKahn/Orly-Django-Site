# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'SpecialEffects.thumbnail_sprite_offset_top'
        db.add_column(u'special_effects_specialeffects', 'thumbnail_sprite_offset_top',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'SpecialEffects.sprite'
        db.add_column(u'special_effects_specialeffects', 'sprite',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['portfolio.Sprite']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'SpecialEffects.thumbnail_sprite_offset_top'
        db.delete_column(u'special_effects_specialeffects', 'thumbnail_sprite_offset_top')

        # Deleting field 'SpecialEffects.sprite'
        db.delete_column(u'special_effects_specialeffects', 'sprite_id')


    models = {
        u'portfolio.sprite': {
            'Meta': {'object_name': 'Sprite'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'special_effects.specialeffects': {
            'Meta': {'ordering': "['position']", 'object_name': 'SpecialEffects'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imgfile': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'sprite': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['portfolio.Sprite']"}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'thumbnail_sprite_offset_top': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['special_effects']