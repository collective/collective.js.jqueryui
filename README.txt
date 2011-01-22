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

include condition and optimizations
===================================

By default this add-on add JQueryUI resources (js and css) on every pages,
but with an include condition that let you configure it.
It can be configured throw the portal_properties.

If your website use jqueryui for only one view or template you can optimize it
by turning off the global include and add your templates. For example:

    <property name="global_include" type="boolean">False</property>
    <property name="views_and_templates" type="lines">
        <element value="mytemplate_view"/>
        <element value="@@myview"/>
    </property>

If you know you need jqueryui on all pages, the best solution is to remove the
expression condition on all jqueryui resources.

TODO:
* add a plone control panel to swith to the best solution.
* use plone.app.registry

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
At the moment you should prefer to use the 1.7.X version of jqueryui
(same package exists for 1.7 branch)
