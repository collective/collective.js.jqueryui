Introduction
============

Integration of jQueryUI in Plone

IMPORTANT - 2.2.0 > 4.0.0 Upgrade
=================================

Can not be upgraded from 2.2.0 directly! It is a major braking release!

There is no upgrade step provided for this "version jump", instead follow these steps:


1. First uninstall 2.1.8 version of JQuery UI using "Site Setup / Add-ons" page. This will cleanly remove all: Plugin selection related registry records; Old style `jsregistry` items; Actions and controlpanel pages.
2. Run the buildout to get the 4.0.0 version.
3. Restart instance.
4. Install JQuery UI again using "Site Setup / Add-ons" page.

WARNINGS
========

Plone < 5
---------

Support is dropped for older versions of Plone and Python 2.7.

Integration for Zope
--------------------

This package can be used as a Plone add-on only.

Usage
=====

buildout.cfg::

    [instance]
    eggs +=
         collective.js.jqueryui


Include plugins and optimizations
=================================

By default this addon register all plugins and activate all of them. The registry based plugin activation is dropped. See https://github.com/collective/collective.js.jqueryui/issues/46.

Credits and contributions
=========================

|makinacom|_

* `Makina Corpus <https://www.makina-corpus.com>`_
* `Ecreall <https://www.ecreall.com>`_

.. |makinacom| image:: http://depot.makina-corpus.org/public/logo.gif
.. _makinacom:  https://www.makina-corpus.com