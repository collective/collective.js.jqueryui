Introduction
============

Integration of jQueryUI in Plone 4.

This version includes jQueryUI 1.8.16 without the tabs plugin.

It is different from collective.jqueryui in many ways:

* no skin dirs (js and css are in resource dirs)
* no all the bunch of files and documentations from original jQueryUI
* this one is minified
* just add all jQueryUI to portal_js, and default css to portal_css (if you 
  apply the profile)

To have an example of the current integration you can check @@example.jqueryui
page. You must activate example within portal_properties.

WARNINGS
========

For Plone 3 you need version 1.7.x of this package

JQueryUI > 1.8.6 is supposed to be compatible with jQuery 1.3.2.
At the moment you should prefer to use the 1.7.X version of jQueryUI
(same package exists for 1.7 branch)

include plugins and optimizations
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

* `Planet Makina Corpus <http://www.makina-corpus.org>`_  `Contact us <mailto:python@makina-corpus.org>`_
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

.. |makinacom| image:: http://depot.makina-corpus.org/public/logo.gif
.. _makinacom:  http://www.makina-corpus.com

