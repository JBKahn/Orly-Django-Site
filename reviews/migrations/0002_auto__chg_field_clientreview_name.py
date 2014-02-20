# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'ClientReview.name'
        db.alter_column(u'reviews_clientreview', 'name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

    def backwards(self, orm):

        # Changing field 'ClientReview.name'
        db.alter_column(u'reviews_clientreview', 'name', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

    models = {
        u'reviews.clientreview': {
            'Meta': {'object_name': 'ClientReview'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['reviews']