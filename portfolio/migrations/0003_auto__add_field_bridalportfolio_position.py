# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'BridalPortfolio.position'
        db.add_column(u'portfolio_bridalportfolio', 'position',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'BridalPortfolio.position'
        db.delete_column(u'portfolio_bridalportfolio', 'position')


    models = {
        u'portfolio.bridalportfolio': {
            'Meta': {'ordering': "['position']", 'object_name': 'BridalPortfolio'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imgfile': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['portfolio']