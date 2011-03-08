from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from openerp-connector import utils

#import datetime

class Transaction(models.Model):
	"""
	Add transaction number in django database
	"""
	number = models.CharField(_('Transaction Number'), max_length=50)
	creation_date = models.DateTimeField(_('Creation'))
	validation_date = models.DateTimeField(_('Validation'))

class UsersLinkTable(models.Model):
	"""
	Link between OpenERP users and Django users
	"""
	openerp_user = models.IntegerField()
	django_user = models.ForeignKey(User)

class AccountingEntry(models.Model):
	"""
	See payments in the django admin
	"""
	lastname = models.CharField(_('Last name'), max_length=60)
	nickname = models.CharField(_('Nickname'), max_length=60)
# Recuperer le nickname de la table d association
	transaction_number = models.CharField(_('Transaction Number'), max_length=50)
	payment_datetime = models.DateTimeField(_('Payment date & time'))
	amount = models.FloatField(_('Amount'), max_length=9)
	nature = models.CharField(_('Payment Type'), max_length=50)

	def __unicode__(self):
		return u'%s %s %s' % (self.lastname, self.transaction_number, self.nature)

#	def save(self, *args, **kwargs):
#		pass
