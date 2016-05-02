# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Store'
        db.create_table(u'core_store', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'core', ['Store'])

        # Adding model 'Category'
        db.create_table(u'core_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('store', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Store'])),
        ))
        db.send_create_signal(u'core', ['Category'])

        # Adding model 'Product'
        db.create_table(u'core_product', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('store', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Store'])),
        ))
        db.send_create_signal(u'core', ['Product'])

        # Adding M2M table for field categories on 'Product'
        m2m_table_name = db.shorten_name(u'core_product_categories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('product', models.ForeignKey(orm[u'core.product'], null=False)),
            ('category', models.ForeignKey(orm[u'core.category'], null=False))
        ))
        db.create_unique(m2m_table_name, ['product_id', 'category_id'])

        # Adding model 'Image'
        db.create_table(u'core_image', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(related_name='images', to=orm['core.Product'])),
        ))
        db.send_create_signal(u'core', ['Image'])

        # Adding model 'Order'
        db.create_table(u'core_order', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('total', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('order_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('customer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('store', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Store'])),
        ))
        db.send_create_signal(u'core', ['Order'])

        # Adding model 'OrderLine'
        db.create_table(u'core_orderline', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Product'])),
            ('quantity', self.gf('django.db.models.fields.IntegerField')()),
            ('order', self.gf('django.db.models.fields.related.ForeignKey')(related_name='order_lines', to=orm['core.Order'])),
        ))
        db.send_create_signal(u'core', ['OrderLine'])


    def backwards(self, orm):
        # Deleting model 'Store'
        db.delete_table(u'core_store')

        # Deleting model 'Category'
        db.delete_table(u'core_category')

        # Deleting model 'Product'
        db.delete_table(u'core_product')

        # Removing M2M table for field categories on 'Product'
        db.delete_table(db.shorten_name(u'core_product_categories'))

        # Deleting model 'Image'
        db.delete_table(u'core_image')

        # Deleting model 'Order'
        db.delete_table(u'core_order')

        # Deleting model 'OrderLine'
        db.delete_table(u'core_orderline')


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
        u'core.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'store': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Store']"})
        },
        u'core.image': {
            'Meta': {'object_name': 'Image'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': u"orm['core.Product']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'core.order': {
            'Meta': {'object_name': 'Order'},
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order_date': ('django.db.models.fields.DateTimeField', [], {}),
            'store': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Store']"}),
            'total': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'})
        },
        u'core.orderline': {
            'Meta': {'object_name': 'OrderLine'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'order_lines'", 'to': u"orm['core.Order']"}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Product']"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {})
        },
        u'core.product': {
            'Meta': {'object_name': 'Product'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.Category']", 'symmetrical': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'store': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Store']"})
        },
        u'core.store': {
            'Meta': {'object_name': 'Store'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['core']