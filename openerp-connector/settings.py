# Django connector-OpenERP settings file.
#
# Please consult the docs for more information about each setting.

from django.conf import settings

OPENERP_HOST = getattr(settings,
						'OPENERP_HOST',
						None)

OPENERP_PORT = getattr(settings,
						'OPENERP_PORT',
						8069)

OPENERP_DB = getattr(settings,
						'OPENERP_DB',
						None)

OPENERP_USER = getattr(settings,
						'OPENERP_USER',
						None)

OPENERP_PASSWD = getattr(settings,
						'OPENERP_PASSWD',
						None)


