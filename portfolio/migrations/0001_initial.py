# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'BridalPortfolio'
        db.create_table(u'portfolio_bridalportfolio', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('imgfile', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'portfolio', ['BridalPortfolio'])


    def backwards(self, orm):
        # Deleting model 'BridalPortfolio'
        db.delete_table(u'portfolio_bridalportfolio')


    models = {
        u'portfolio.bridalportfolio': {
            'Meta': {'object_name': 'BridalPortfolio'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imgfile': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['portfolio']