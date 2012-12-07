from setuptools import setup

version = '0.1.dev'

long_description = '\n\n'.join([
    open('README.rst').read(),
    open('CREDITS.rst').read(),
#    open('CHANGES.rst').read(),
    ])

install_requires = [
    'flask',
    'flask-bootstrap',
    'numpy',
    'PIL',
    'setuptools',
    'Flask==0.9',
    'Flask-DebugToolbar==0.7.1',
    'Flask-Uploads==0.1.3',
    'Flask-WTF==0.8',
    'Jinja2==2.6',
    'WTForms==1.0.2',
    'Werkzeug==0.8.3',
    'blinker==1.2',
    'httplib2==0.7.6',
    'ordereddict==1.1',
    'requests==0.14.1',
    'yolk==0.4.3',
    ],

tests_require = [
    ]

setup(name='crumble',
      version=version,
      description="TODO",
      long_description=long_description,
      # Get strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[],
      keywords=[],
      author='TODO',
      author_email='info@technokrat.nl',
      url='',
      license='BSD',
      packages=['crumble'],
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      tests_require=tests_require,
      extras_require = {'test': tests_require},
      entry_points={
          'console_scripts': [
              'runserver = crumble.main:go',
              'runlemon = run:main',
          ]},
      )
