# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ClientReview.thumbnail'
        db.add_column(u'reviews_clientreview', 'thumbnail',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=500, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ClientReview.thumbnail_sprite_offset_top'
        db.add_column(u'reviews_clientreview', 'thumbnail_sprite_offset_top',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'ClientReview.sprite'
        db.add_column(u'reviews_clientreview', 'sprite',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['core.Sprite']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ClientReview.thumbnail'
        db.delete_column(u'reviews_clientreview', 'thumbnail')

        # Deleting field 'ClientReview.thumbnail_sprite_offset_top'
        db.delete_column(u'reviews_clientreview', 'thumbnail_sprite_offset_top')

        # Deleting field 'ClientReview.sprite'
        db.delete_column(u'reviews_clientreview', 'sprite_id')


    models = {
        u'core.sprite': {
            'Meta': {'object_name': 'Sprite'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'reviews.clientreview': {
            'Meta': {'ordering': "['position']", 'object_name': 'ClientReview'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'sprite': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Sprite']"}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'thumbnail_sprite_offset_top': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['reviews']