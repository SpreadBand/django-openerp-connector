from openerp_dj_conn.models import AccountingEntry
from django.contrib import admin

class ConnectorAdmin(admin.ModelAdmin):

	fields = ['lastname', 'nickname', 'transaction_number', 'payment_datetime', 'nature', 'amount']
	list_display = ('lastname', 'nickname', 'transaction_number', 'payment_datetime', 'nature', 'amount')
	list_filter = ['payment_datetime', 'nature', 'lastname', 'nickname']
	search_fields = ['transaction_number', 'lastname', 'nickname']
	date_hierarchy = 'payment_datetime'

admin.site.register(AccountingEntry, ConnectorAdmin)
