# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Question'
        db.delete_table('polls_question')

        # Adding model 'Qudaestion'
        db.create_table('polls_qudaestion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question_text', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('polls', ['Qudaestion'])


        # Changing field 'Choice.question'
        db.alter_column('polls_choice', 'question_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['polls.Qudaestion']))

    def backwards(self, orm):
        # Adding model 'Question'
        db.create_table('polls_question', (
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question_text', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('polls', ['Question'])

        # Deleting model 'Qudaestion'
        db.delete_table('polls_qudaestion')


        # Changing field 'Choice.question'
        db.alter_column('polls_choice', 'question_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['polls.Question']))

    models = {
        'polls.choice': {
            'Meta': {'object_name': 'Choice'},
            'choice_text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['polls.Qudaestion']"}),
            'votes': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'polls.qudaestion': {
            'Meta': {'object_name': 'Qudaestion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'question_text': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['polls']