from distutils.core import setup


setup(
    name = "django-openerp-connector",
    author = "Guillaume Delpierre",
    author_email = "gdelpierre@spreadband.com",
    description = "Bridge between django and OpenERP",
    long_description = open("README.rst").read(),
    license = "GPL v3",
    url = "https://github.com/SpreadBand/django-openerp-connector",
    packages = [
        "openerp_connector",
    ],
    include_package_data = True,
    package_data = {
        'openerp_connector': [
            'locale/*/*/*',
        ]
    },
    zip_safe=False,
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GPL License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ]
)
