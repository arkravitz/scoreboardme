# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'EventRequest.event_request'
        db.delete_column(u'events_eventrequest', 'event_request_id')

        # Deleting field 'EventRequest.request_to'
        db.delete_column(u'events_eventrequest', 'request_to_id')

        # Adding field 'EventRequest.event'
        db.add_column(u'events_eventrequest', 'event',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['events.Event']),
                      keep_default=False)

        # Adding field 'EventRequest.profile'
        db.add_column(u'events_eventrequest', 'profile',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['core.UserProfile']),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'EventRequest.event_request'
        db.add_column(u'events_eventrequest', 'event_request',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['events.Event']),
                      keep_default=False)

        # Adding field 'EventRequest.request_to'
        db.add_column(u'events_eventrequest', 'request_to',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['core.UserProfile']),
                      keep_default=False)

        # Deleting field 'EventRequest.event'
        db.delete_column(u'events_eventrequest', 'event_id')

        # Deleting field 'EventRequest.profile'
        db.delete_column(u'events_eventrequest', 'profile_id')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'core.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'currency': ('django.db.models.fields.IntegerField', [], {'default': '1000'}),
            'event_requests': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'requested_users'", 'symmetrical': 'False', 'through': u"orm['events.EventRequest']", 'to': u"orm['events.Event']"}),
            'events': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'participants'", 'blank': 'True', 'through': u"orm['events.Score']", 'to': u"orm['events.Event']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'profile'", 'unique': 'True', 'to': u"orm['auth.User']"})
        },
        u'events.event': {
            'Meta': {'object_name': 'Event'},
            'bet_amount': ('django.db.models.fields.IntegerField', [], {}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'created_events'", 'to': u"orm['core.UserProfile']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'ended': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '70'})
        },
        u'events.eventrequest': {
            'Meta': {'object_name': 'EventRequest'},
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.Event']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'optional_message': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.UserProfile']"})
        },
        u'events.score': {
            'Meta': {'unique_together': "(('event', 'participant'),)", 'object_name': 'Score'},
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.Event']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'participant': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.UserProfile']"}),
            'score': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['events']