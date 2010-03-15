from setuptools import setup, find_packages
import os

version = '1.7.2.7'

setup(name='collective.js.jqueryui',
      version=version,
      description="JQueryUI ready to be included in portal_javascript",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='JeanMichel FRANCOIS aka toutpt',
      author_email='jeanmichel.francois@makina-corpus.com',
      url='https://svn.plone.org/svn/collective/collective.js.jqueryui',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', 'collective.js'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'collective.js.jquery'
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
