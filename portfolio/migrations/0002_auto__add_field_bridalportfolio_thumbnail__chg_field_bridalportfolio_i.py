# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'BridalPortfolio.thumbnail'
        db.add_column(u'portfolio_bridalportfolio', 'thumbnail',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=500, null=True, blank=True),
                      keep_default=False)


        # Changing field 'BridalPortfolio.imgfile'
        db.alter_column(u'portfolio_bridalportfolio', 'imgfile', self.gf('django.db.models.fields.files.ImageField')(max_length=100))

    def backwards(self, orm):
        # Deleting field 'BridalPortfolio.thumbnail'
        db.delete_column(u'portfolio_bridalportfolio', 'thumbnail')


        # Changing field 'BridalPortfolio.imgfile'
        db.alter_column(u'portfolio_bridalportfolio', 'imgfile', self.gf('django.db.models.fields.files.FileField')(max_length=100))

    models = {
        u'portfolio.bridalportfolio': {
            'Meta': {'object_name': 'BridalPortfolio'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imgfile': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['portfolio']