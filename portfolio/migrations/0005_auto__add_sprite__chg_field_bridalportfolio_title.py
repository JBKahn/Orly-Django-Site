# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Sprite'
        db.create_table(u'portfolio_sprite', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'portfolio', ['Sprite'])


        # Changing field 'BridalPortfolio.title'
        db.alter_column(u'portfolio_bridalportfolio', 'title', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

    def backwards(self, orm):
        # Deleting model 'Sprite'
        db.delete_table(u'portfolio_sprite')


        # Changing field 'BridalPortfolio.title'
        db.alter_column(u'portfolio_bridalportfolio', 'title', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

    models = {
        u'portfolio.bridalportfolio': {
            'Meta': {'ordering': "['position']", 'object_name': 'BridalPortfolio'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imgfile': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        u'portfolio.sprite': {
            'Meta': {'object_name': 'Sprite'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['portfolio']