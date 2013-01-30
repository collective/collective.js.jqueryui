Introduction
============

Integration of jQueryUI in Plone 4.3.

Version: 1.10.0

WARNINGS
========

Plone < 4
---------

For Plone 3 you need version 1.7.x of this package

JQueryUI > 1.8.6 is supposed to be compatible with jQuery 1.3.2.
At the moment you should prefer to use the 1.7.X version of jQueryUI
(same package exists for 1.7 branch)

Plone < 4.3
-----------

Use version < 1.9

Integration for Zope and Plone
==============================
This package can be used as a Plone add-on - for this it adds GenericSetup
profiles and Plone ControlPanel configlets - or it can be used as a simple Zope
jQuery UI resources registrar. See bellow how your zc.buildout config file
should look like if you use collective.js.jqueryui with or without Plone.


Plone
-----
for Plone > 4.0:

buildout.cfg::

    [instance]
    eggs +=
         collective.js.jqueryui

for Plone == 4.0 you must add plone.app.registry yourself:

buildout.cfg::

    extends=http://good-py.appspot.com/release/plone.app.registry/1.0b2
    [instance]
    eggs +=
        collective.js.jqueryui
        plone.app.registry

Zope
----
buildout.cfg::

    [instance]
    eggs =
        collective.js.jqueryui
    zcml =
        collective.js.jqueryui




Include plugins and optimizations
=================================

By default this addon register all plugins and activate all of them except tabs.
So ui.tabs is registred but not activated.

Because jQueryUI is big on both javascripts and css you may want to optimize
the configuration of your site or your addon which depends on this one.

So you can activate/unactivate plugins using registry profile or the jQueryUI
controlpanel.

Using registry.xml, you can activate only what you want:

::

    <registry>
        <records interface="collective.js.jqueryui.controlpanel.IJQueryUIPlugins">
          <value key="ui_draggable">True</value>
          <value key="ui_droppable">True</value>
        </records>
    </registry>

In the case of a policy you can do a full configuration:

::

    <registry>
        <records interface="collective.js.jqueryui.controlpanel.IJQueryUIPlugins">
          <value key="ui_core">True</value>
          <value key="ui_widget">True</value>
          <value key="ui_mouse">True</value>
          <value key="ui_position">True</value>
          <value key="ui_draggable">True</value>
          <value key="ui_droppable">True</value>
          <value key="ui_resizable">True</value>
          <value key="ui_selectable">True</value>
          <value key="ui_sortable">True</value>
          <value key="ui_accordion">False</value>
          <value key="ui_autocomplete">False</value>
          <value key="ui_button">False</value>
          <value key="ui_dialog">False</value>
          <value key="ui_slider">False</value>
          <value key="ui_tabs">False</value>
          <value key="ui_datepicker">False</value>
          <value key="ui_progressbar">False</value>
          <value key="effects_core">False</value>
          <value key="effects_blind">False</value>
          <value key="effects_bounce">False</value>
          <value key="effects_clip">False</value>
          <value key="effects_drop">False</value>
          <value key="effects_explode">False</value>
          <value key="effects_fade">False</value>
          <value key="effects_fold">False</value>
          <value key="effects_highlight">False</value>
          <value key="effects_pulsate">False</value>
          <value key="effects_scale">False</value>
          <value key="effects_shake">False</value>
          <value key="effects_slide">False</value>
          <value key="effects_transfer">False</value>
        </records>
        <records interface="collective.js.jqueryui.controlpanel.IJQueryUICSS">
          <value key="css">False</value>
          <value key="patch">False</value>
        </records>
    </registry>

Using the control panel, you can select plugins you want. If you unselect a
plugin it will be unactivated (but not its dependencies)

Using python, you just have to use plone.registry api:

::

    from zope.component import getUtility
    from plone.registry.interfaces import IRegistry
    from collective.js.jqueryui.config import DEPS
    from collective.js.jqueryui.interfaces import IJQueryUICSS, IJQueryUIPlugins
    #is plone.app.registry
    registry = getUtility(IRegistry)
    proxy = registry.forInterface(IJQueryUIPlugins)
    setattr(proxy, 'ui_draggable', True)
    setattr(proxy, 'ui_droppable', True)


Credits and contributions
=========================

|makinacom|_

* `Makina Corpus <http://www.makina-corpus.com>`_
* `Ecreall <http://www.ecreall.com>`_

Contributors
============

* Vincent Fretin [vincentfretin]
* Hanno Schlichting [hanno]
* Nathan Vangheem [vangheem]
* Marcos F. Romero [marcosfromero]
* Kees Hink [khink]
* Robert Niederreiter [rnix]
* JeanMichel FRANCOIS [toutpt]
* Alin Voinea [avoinea]

.. |makinacom| image:: http://depot.makina-corpus.org/public/logo.gif
.. _makinacom:  http://www.makina-corpus.com
