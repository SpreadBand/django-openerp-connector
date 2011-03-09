#!/usr/bin/env pythoni
# -*- coding: utf-8 -*-

from django.conf import settings
from openerp_connector import settings as openerp_settings

import xmlrpclib

host_openerp = openerp_settings.OPENERP_HOST
port_openerp = openerp_settings.OPENERP_PORT
db_openerp = openerp_settings.OPENERP_DB
user_openerp = openerp_settings.OPENERP_USER
passwd_openerp = openerp_settings.OPENERP_PASSWD
url_common ='http://%s:%d/xmlrpc/common' %(host_openerp,port_openerp)
url_object ='http://%s:%d/xmlrpc/object' %(host_openerp,port_openerp)


def openerp_connect():
	"""
	Connect to the OpenERP API.
	"""
	sock_common = xmlrpclib.ServerProxy(url_common)
	uid = sock_common.login(db_openerp, user_openerp, passwd_openerp)
	return uid

def sock_object_execute(resource_path, action_name, *args, **kwargs):
	"""
	Define sock_object
	"""	
	sock_object = xmlrpclib.ServerProxy(url_object)
	sock_object_execute = sock_object.execute(db_openerp, openerp_connect(), passwd_openerp, resource_path, action_name, *args, **kwargs)
	return sock_object_execute
	
def openerp_create_client(name, lang, zipcode, city, email):
	"""
	Create a new client in OpenERP Database
	lang = fr_FR
	"""
	partner = {
		'name' : name,
		'lang' : lang,
	}
	partner_id = sock_object_execute('res.partner', 'create', partner)

	address = {
		'partner_id' : partner_id,
		'zip' : zipcode,
		'city' : city,
		'email' : email,
	}
	address_id = sock_object_execute('res.partner.address', 'create', address)

def client_id_openerp(get_openerp_client_id):
	"""
	Define client_id
	"""
	args = [(
		'id','=' , get_openerp_client_id
	)]
	ids = sock_object_execute('res.partner', 'search', args)
	return ids

def openerp_client_search(client_id_openerp):
	"""
	Search with its id a client in OpenERP Database
	"""
 	fields = [
		'name',
     	'user_id',
     	'email'
 	]
 	partner_data = sock_object_execute('res.partner', 'read', client_id_openerp, fields)
	return partner_data

# def openerp_accounting_entry(client_id_openerp, credit_amount, payment_datetime, payment_nature, transaction_number):
	"""
	Add an accounting entry to the OpenERP Database
	"""
#	values = { 
#		'' : credit_amount, 
#		'' : payment_datetime,
#		'' : payment_nature,
#		'' : transaction_number,
#	}
#	accounting_entry_result = sock_object_execute('res.partner', 'write', client_id_openerp, values)
#	return accounting_entry_result 
