from setuptools import setup, find_packages
import os

version = '2.1.4'

setup(
    name='collective.js.jqueryui',
    version=version,
    description="JQueryUI ready for Plone",
    long_description=open("README.rst").read() + "\n" +
         open(os.path.join("docs", "UPGRADE.txt")).read() + "\n" +
         open("CHANGES.rst").read(),
    classifiers=[
        "Environment :: Web Environment",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        "Framework :: Zope2",
        "Framework :: Zope :: 2",
        "Framework :: Zope :: 4",
        "Framework :: Plone",
        "Framework :: Plone :: Addon",
        "Framework :: Plone :: 4.3",
        "Framework :: Plone :: 5.0",
        "Framework :: Plone :: 5.1",
        "Framework :: Plone :: 5.2",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    keywords='plone jqueryui',
    author='JeanMichel FRANCOIS aka toutpt',
    author_email='toutpt@gmail.com',
    url='https://github.com/collective/collective.js.jqueryui',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['collective', 'collective.js'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'plone.app.jquery > 1.6',
        'Products.CMFPlone',
        'setuptools',
    ],
    setup_requires=["setuptools_git"],
    extras_require={},
    entry_points="""
    # -*- Entry points: -*-
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
