Introduction
============

Integration of jqueryui in Plone 3.3 and 4.

This version includes jqueryui 1.8.7 without the tabs plugin.

It is different from collective.jqueryui in many ways:

* no skin dirs (js and css are in resource dirs)
* no all the bunch of files and documentations from original jqueryui
* this one is minified
* just add all jqueryui to portal_js, and default css to portal_css (if you 
  apply the profile)

To have an example of the current integration you can check @@example.jqueryui
page

Credits
=======

|makinacom|_

* `Planet Makina Corpus <http://www.makina-corpus.org>`_
* `Contact us <mailto:python@makina-corpus.org>`_
* Contributions by Vincent Fretin (`Ecreall <http://www.ecreall.com>`_)

.. |makinacom| image:: http://depot.makina-corpus.org/public/logo.gif
.. _makinacom:  http://www.makina-corpus.com

Notes
=====

The package contains now only one profile. It doesn't replace
the jQuery version like the previous versions did.

WARNINGS
========

JQueryUI > 1.8.6 is supposed to be compatible with jQuery 1.3.2.
On example page every things are working except Dialog. So at the
moment you would prefer use the 1.7.X version of jqueryui (same package
exists for 1.7 branch.

Upgrade notes
=============

If you used the ``withjqtools`` or ``withjqtoolsplone3`` profile in older
version, please use now the ``default`` profile.
