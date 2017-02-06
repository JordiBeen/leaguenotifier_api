import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'pyramid',
    'SQLAlchemy',
    'pyramid_chameleon',
    'pyramid_debugtoolbar',
    'pyramid_tm',
    'pyramid_mako',
    'python-magic',
    'python-dateutil',
    'psycopg2',
    'transaction',
    'zope.sqlalchemy',
    'pyramid_beaker',
    'marshmallow==1.2.4',
    'itsdangerous',
    'GeoAlchemy2',
    'bcrypt',
    'pycrypto',
    'waitress'
]

setup(name='leaguenotifier',
      version='0.0.1',
      description='leaguenotifier',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
          "Programming Language :: Python",
          "Framework :: Pyramid",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
      ],
      author='',
      author_email='',
      url='',
      keywords='web pyramid pylons',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="leaguenotifier",
      entry_points="""\
      [paste.app_factory]
      main = leaguenotifier:main
      [console_scripts]
      initialize_leaguenotifier_db = leaguenotifier.scripts.initializedb:main
      drop_leaguenotifier_db = leaguenotifier.scripts.dropdb:main
      """,
      )
