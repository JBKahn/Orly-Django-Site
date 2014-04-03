# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ClientReview'
        db.create_table(u'reviews_clientreview', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('thumbnail', self.gf('django.db.models.fields.files.ImageField')(max_length=500, null=True, blank=True)),
            ('position', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('thumbnail_sprite_offset_top', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('sprite', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Sprite'])),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'reviews', ['ClientReview'])


    def backwards(self, orm):
        # Deleting model 'ClientReview'
        db.delete_table(u'reviews_clientreview')


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