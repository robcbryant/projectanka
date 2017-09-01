# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FormProject'
        db.create_table(u'maqluengine_formproject', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('uri_img', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('uri_thumbnail', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('uri_download', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('uri_upload', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('uri_upload_key', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('geojson_string', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('is_public', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='project_ref_to_user_creator', null=True, on_delete=models.SET_NULL, to=orm['auth.User'])),
            ('date_last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='project_ref_to__user_modifier', null=True, on_delete=models.SET_NULL, to=orm['auth.User'])),
        ))
        db.send_create_signal(u'maqluengine', ['FormProject'])

        # Adding model 'FormTypeGroup'
        db.create_table(u'maqluengine_formtypegroup', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='formtypegroup_ref_to_user_creator', null=True, on_delete=models.SET_NULL, to=orm['auth.User'])),
            ('date_last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='formtypegroup_ref_to_user_modifier', null=True, on_delete=models.SET_NULL, to=orm['auth.User'])),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maqluengine.FormProject'])),
        ))
        db.send_create_signal(u'maqluengine', ['FormTypeGroup'])

        # Adding model 'FormType'
        db.create_table(u'maqluengine_formtype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('form_type_name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.IntegerField')()),
            ('media_type', self.gf('django.db.models.fields.IntegerField')(default=-1)),
            ('file_extension', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('uri_prefix', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('is_hierarchical', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_public', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='formtype_ref_to_user_creator', null=True, on_delete=models.SET_NULL, to=orm['auth.User'])),
            ('date_last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='formtype_ref_to_user_modifier', null=True, on_delete=models.SET_NULL, to=orm['auth.User'])),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maqluengine.FormProject'])),
            ('form_type_group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maqluengine.FormTypeGroup'], null=True, blank=True)),
        ))
        db.send_create_signal(u'maqluengine', ['FormType'])

        # Adding model 'FormRecordAttributeType'
        db.create_table(u'maqluengine_formrecordattributetype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('record_type', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('form_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maqluengine.FormType'], blank=True)),
            ('order_number', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maqluengine.FormProject'])),
            ('is_public', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='frat_ref_to_user_creator', null=True, on_delete=models.SET_NULL, to=orm['auth.User'])),
            ('date_last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='frat_ref_to_user_modifier', null=True, on_delete=models.SET_NULL, to=orm['auth.User'])),
        ))
        db.send_create_signal(u'maqluengine', ['FormRecordAttributeType'])

        # Adding model 'FormRecordReferenceType'
        db.create_table(u'maqluengine_formrecordreferencetype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('record_type', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('order_number', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('is_public', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maqluengine.FormProject'])),
            ('form_type_parent', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='ref_to_parent_formtype', null=True, to=orm['maqluengine.FormType'])),
            ('form_type_reference', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='ref_to_value_formtype', null=True, on_delete=models.SET_NULL, to=orm['maqluengine.FormType'])),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='frrt_ref_to_user_creator', null=True, on_delete=models.SET_NULL, to=orm['auth.User'])),
            ('date_last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='frrt_ref_to_user_modifier', null=True, on_delete=models.SET_NULL, to=orm['auth.User'])),
        ))
        db.send_create_signal(u'maqluengine', ['FormRecordReferenceType'])

        # Adding model 'Form'
        db.create_table(u'maqluengine_form', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('form_name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('form_number', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('form_geojson_string', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('hierarchy_parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maqluengine.Form'], null=True, on_delete=models.SET_NULL, blank=True)),
            ('is_public', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maqluengine.FormProject'])),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='form_ref_to_user_creator', null=True, on_delete=models.SET_NULL, to=orm['auth.User'])),
            ('date_last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='form_ref_to_user_modifier', null=True, on_delete=models.SET_NULL, to=orm['auth.User'])),
            ('sort_index', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('form_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maqluengine.FormType'])),
        ))
        db.send_create_signal(u'maqluengine', ['Form'])

        # Adding model 'FormRecordAttributeValue'
        db.create_table(u'maqluengine_formrecordattributevalue', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('record_value', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='formatt_ref_to_user_creator', null=True, on_delete=models.SET_NULL, to=orm['auth.User'])),
            ('date_last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='formatt_ref_to_user_modifier', null=True, on_delete=models.SET_NULL, to=orm['auth.User'])),
            ('record_attribute_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maqluengine.FormRecordAttributeType'])),
            ('form_parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maqluengine.Form'], null=True, blank=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maqluengine.FormProject'])),
        ))
        db.send_create_signal(u'maqluengine', ['FormRecordAttributeValue'])

        # Adding model 'FormRecordReferenceValue'
        db.create_table(u'maqluengine_formrecordreferencevalue', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('external_key_reference', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('form_parent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='ref_to_parent_form', to=orm['maqluengine.Form'])),
            ('record_reference_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maqluengine.FormRecordReferenceType'])),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maqluengine.FormProject'])),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='formref_ref_to_user_creator', null=True, on_delete=models.SET_NULL, to=orm['auth.User'])),
            ('date_last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='formref_ref_to_user_modifier', null=True, on_delete=models.SET_NULL, to=orm['auth.User'])),
        ))
        db.send_create_signal(u'maqluengine', ['FormRecordReferenceValue'])

        # Adding M2M table for field record_reference on 'FormRecordReferenceValue'
        m2m_table_name = db.shorten_name(u'maqluengine_formrecordreferencevalue_record_reference')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('formrecordreferencevalue', models.ForeignKey(orm[u'maqluengine.formrecordreferencevalue'], null=False)),
            ('form', models.ForeignKey(orm[u'maqluengine.form'], null=False))
        ))
        db.create_unique(m2m_table_name, ['formrecordreferencevalue_id', 'form_id'])

        # Adding model 'Permissions'
        db.create_table(u'maqluengine_permissions', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maqluengine.FormProject'], null=True, blank=True)),
            ('access_level', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('job_title', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'maqluengine', ['Permissions'])

        # Adding model 'AJAXRequestData'
        db.create_table(u'maqluengine_ajaxrequestdata', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('is_finished', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('keep_alive', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('jsonString', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'maqluengine', ['AJAXRequestData'])


    def backwards(self, orm):
        # Deleting model 'FormProject'
        db.delete_table(u'maqluengine_formproject')

        # Deleting model 'FormTypeGroup'
        db.delete_table(u'maqluengine_formtypegroup')

        # Deleting model 'FormType'
        db.delete_table(u'maqluengine_formtype')

        # Deleting model 'FormRecordAttributeType'
        db.delete_table(u'maqluengine_formrecordattributetype')

        # Deleting model 'FormRecordReferenceType'
        db.delete_table(u'maqluengine_formrecordreferencetype')

        # Deleting model 'Form'
        db.delete_table(u'maqluengine_form')

        # Deleting model 'FormRecordAttributeValue'
        db.delete_table(u'maqluengine_formrecordattributevalue')

        # Deleting model 'FormRecordReferenceValue'
        db.delete_table(u'maqluengine_formrecordreferencevalue')

        # Removing M2M table for field record_reference on 'FormRecordReferenceValue'
        db.delete_table(db.shorten_name(u'maqluengine_formrecordreferencevalue_record_reference'))

        # Deleting model 'Permissions'
        db.delete_table(u'maqluengine_permissions')

        # Deleting model 'AJAXRequestData'
        db.delete_table(u'maqluengine_ajaxrequestdata')


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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'maqluengine.ajaxrequestdata': {
            'Meta': {'object_name': 'AJAXRequestData'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_finished': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'jsonString': ('django.db.models.fields.TextField', [], {}),
            'keep_alive': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        u'maqluengine.form': {
            'Meta': {'object_name': 'Form'},
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'form_ref_to_user_creator'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['auth.User']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'date_last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'form_geojson_string': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'form_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'form_number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'form_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['maqluengine.FormType']"}),
            'hierarchy_parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['maqluengine.Form']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'form_ref_to_user_modifier'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['auth.User']"}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['maqluengine.FormProject']"}),
            'sort_index': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'maqluengine.formproject': {
            'Meta': {'object_name': 'FormProject'},
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'project_ref_to_user_creator'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['auth.User']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'date_last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'geojson_string': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'project_ref_to__user_modifier'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['auth.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'uri_download': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'uri_img': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'uri_thumbnail': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'uri_upload': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'uri_upload_key': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'maqluengine.formrecordattributetype': {
            'Meta': {'object_name': 'FormRecordAttributeType'},
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'frat_ref_to_user_creator'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['auth.User']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'date_last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'form_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['maqluengine.FormType']", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'frat_ref_to_user_modifier'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['auth.User']"}),
            'order_number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['maqluengine.FormProject']"}),
            'record_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'maqluengine.formrecordattributevalue': {
            'Meta': {'object_name': 'FormRecordAttributeValue'},
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'formatt_ref_to_user_creator'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['auth.User']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'date_last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'form_parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['maqluengine.Form']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'formatt_ref_to_user_modifier'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['auth.User']"}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['maqluengine.FormProject']"}),
            'record_attribute_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['maqluengine.FormRecordAttributeType']"}),
            'record_value': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'maqluengine.formrecordreferencetype': {
            'Meta': {'object_name': 'FormRecordReferenceType'},
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'frrt_ref_to_user_creator'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['auth.User']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'date_last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'form_type_parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'ref_to_parent_formtype'", 'null': 'True', 'to': u"orm['maqluengine.FormType']"}),
            'form_type_reference': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'ref_to_value_formtype'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['maqluengine.FormType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'frrt_ref_to_user_modifier'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['auth.User']"}),
            'order_number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['maqluengine.FormProject']"}),
            'record_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'maqluengine.formrecordreferencevalue': {
            'Meta': {'object_name': 'FormRecordReferenceValue'},
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'formref_ref_to_user_creator'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['auth.User']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'date_last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'external_key_reference': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'form_parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ref_to_parent_form'", 'to': u"orm['maqluengine.Form']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'formref_ref_to_user_modifier'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['auth.User']"}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['maqluengine.FormProject']"}),
            'record_reference': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'ref_to_value_form'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['maqluengine.Form']"}),
            'record_reference_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['maqluengine.FormRecordReferenceType']"})
        },
        u'maqluengine.formtype': {
            'Meta': {'object_name': 'FormType'},
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'formtype_ref_to_user_creator'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['auth.User']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'date_last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'file_extension': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'form_type_group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['maqluengine.FormTypeGroup']", 'null': 'True', 'blank': 'True'}),
            'form_type_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_hierarchical': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'media_type': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'formtype_ref_to_user_modifier'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['auth.User']"}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['maqluengine.FormProject']"}),
            'type': ('django.db.models.fields.IntegerField', [], {}),
            'uri_prefix': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        u'maqluengine.formtypegroup': {
            'Meta': {'object_name': 'FormTypeGroup'},
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'formtypegroup_ref_to_user_creator'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['auth.User']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'date_last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'formtypegroup_ref_to_user_modifier'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['auth.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['maqluengine.FormProject']"})
        },
        u'maqluengine.permissions': {
            'Meta': {'object_name': 'Permissions'},
            'access_level': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job_title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['maqluengine.FormProject']", 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['maqluengine']