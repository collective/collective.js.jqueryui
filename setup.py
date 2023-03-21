# -*- coding: utf-8 -*-
"""Installer for the collective.js.jqueryui package."""

from setuptools import find_packages
from setuptools import setup


long_description = "\n\n".join(
    [
        open("README.rst").read(),
        open("CONTRIBUTORS.rst").read(),
        open("CHANGES.rst").read(),
    ]
)


setup(
    name="collective.js.jqueryui",
    version="2.2.0",
    description="JQueryUI ready for Plone",
    long_description=long_description,
    # Get more from https://pypi.org/classifiers/
    classifiers=[
        "Development Status :: 6 - Mature",
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
    keywords="plone jqueryui",
    author="JeanMichel FRANCOIS aka toutpt",
    author_email="toutpt@gmail.com",
    url="https://github.com/collective/collective.js.jqueryui",
    project_urls={
        "PyPI": "https://pypi.python.org/pypi/collective.js.jqueryui",
        "Source": "https://github.com/collective/collective.js.jqueryui",
        "Tracker": "https://github.com/collective/collective.js.jqueryui/issues",
        # 'Documentation': 'https://collective.js.jqueryui.readthedocs.io/en/latest/',
    },
    license="GPL version 2",
    packages=find_packages("src", exclude=["ez_setup"]),
    namespace_packages=["collective", "collective.js"],
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    python_requires=">=2.7",
    install_requires=[
        "Products.CMFPlone",
        "setuptools",
    ],
    extras_require={
        "test": [
            "plone.api",
            "plone.app.testing",
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
